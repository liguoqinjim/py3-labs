import psutil
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import threading
import time
import subprocess
from datetime import datetime


class MemoryMonitor:
    def __init__(self, pid=None, process_name=None):
        self.pid = pid
        self.process_name = process_name
        self.memory_data = []
        self.time_data = []
        self.max_points = 30000
        self.start_time = time.time()  # 记录开始监控的时间

        # 如果没有提供pid，则通过进程名查找
        if not self.pid and self.process_name:
            self.pid = self._find_pid_by_name()

        if not self.pid:
            raise ValueError("必须提供进程ID或进程名")

        self.app = dash.Dash(__name__)
        self.setup_dashboard()

    def _find_pid_by_name(self):
        for proc in psutil.process_iter(['name', 'pid']):
            if self.process_name in proc.info['name']:
                return proc.info['pid']
        raise ValueError(f"未找到名为 {self.process_name} 的进程")

    def get_memory_usage(self):
        try:
            process = psutil.Process(self.pid)
            # 获取物理内存使用量(RSS)，转换为MB
            memory_mb = process.memory_info().rss / 1024 / 1024

            # 同时获取额外的内存信息
            memory_info = {
                'rss': memory_mb,  # 常驻内存集
                'vms': process.memory_info().vms / 1024 / 1024,  # 虚拟内存大小
                'percent': process.memory_percent()  # 内存占用百分比
            }
            return memory_info
        except psutil.NoSuchProcess:
            return None

    def setup_dashboard(self):
        self.app.layout = html.Div([
            html.H1('实时进程内存监控'),
            html.Div(id='pid-display', children=f'监控进程PID: {self.pid}'),
            dcc.Graph(id='memory-graph'),
            html.Div(id='memory-stats'),
            dcc.Interval(
                id='interval-component',
                interval=1000 * 5,  # 每秒更新
                n_intervals=0
            )
        ])

        @self.app.callback(
            [Output('memory-graph', 'figure'),
             Output('memory-stats', 'children')],
            [Input('interval-component', 'n_intervals')]
        )
        def update_graph(n):
            memory_info = self.get_memory_usage()
            if memory_info:
                current_time = time.time()
                self.memory_data.append(memory_info['rss'])
                self.time_data.append(current_time)

                # 保持固定数量的数据点
                if len(self.memory_data) > self.max_points:
                    self.memory_data = self.memory_data[-self.max_points:]
                    self.time_data = self.time_data[-self.max_points:]

                # 转换时间戳为可读格式
                readable_times = [
                    datetime.fromtimestamp(t).strftime('%H:%M:%S')
                    for t in self.time_data
                ]

                # 创建内存使用图
                fig = go.Figure(data=[
                    go.Scatter(
                        x=readable_times,
                        y=self.memory_data,
                        mode='lines+markers',
                        name='物理内存(MB)'
                    )
                ])
                fig.update_layout(
                    title='内存使用趋势',
                    xaxis_title='时间',
                    yaxis_title='内存 (MB)',
                    height=500,
                    xaxis=dict(
                        tickmode='auto',
                        nticks=10,
                        tickangle=45
                    )
                )

                # 详细内存统计
                stats = [
                    html.P(f"常驻内存(RSS): {memory_info['rss']:.2f} MB"),
                    html.P(f"虚拟内存(VMS): {memory_info['vms']:.2f} MB"),
                    html.P(f"内存占用比: {memory_info['percent']:.2f}%")
                ]

                return fig, stats

            return go.Figure(), "无法获取内存信息"

    def run(self, port=8050):
        print(f"访问 http://localhost:{port} 查看实时监控")
        self.app.run_server(debug=False, port=port)


def find_celery_worker_pid(app_name):
    """查找Celery worker的进程ID"""
    try:
        # 使用pgrep查找匹配的进程
        result = subprocess.check_output(
            f"pgrep -f 'celery.*{app_name}'",
            shell=True,
            text=True
        ).strip()
        return int(result.split('\n')[0])  # 返回第一个匹配的PID
    except subprocess.CalledProcessError:
        print(f"未找到{app_name} 的Celery worker进程")
        return None


# 使用示例
if __name__ == "__main__":
    # 方法3：查找特定Celery应用的worker
    pid = find_celery_worker_pid('intelligent_recommend')
    if pid:
        monitor = MemoryMonitor(pid=pid)
        monitor.run()
    else:
        print("未找到进程，请检查Celery worker是否正在运行")
