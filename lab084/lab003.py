import psutil
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import threading
import time
import subprocess
from datetime import datetime
from plotly.subplots import make_subplots


class MemoryMonitor:
    def __init__(self, pids=None, process_name=None):
        self.pids = pids if isinstance(pids, list) else [pids] if pids else []
        self.process_name = process_name
        self.memory_data = {pid: [] for pid in self.pids}  # 为每个PID存储内存数据
        self.time_data = {pid: [] for pid in self.pids}    # 为每个PID存储时间数据
        self.max_points = 30000
        self.start_time = time.time()

        # 如果没有提供pid，则通过进程名查找
        if not self.pids and self.process_name:
            self.pids = self._find_pids_by_name()

        if not self.pids:
            raise ValueError("必须提供进程ID或进程名")

        self.app = dash.Dash(__name__)
        self.setup_dashboard()

    def _find_pids_by_name(self):
        pids = []
        for proc in psutil.process_iter(['name', 'pid']):
            if self.process_name in proc.info['name']:
                pids.append(proc.info['pid'])
        if not pids:
            raise ValueError(f"未找到名为 {self.process_name} 的进程")
        return pids

    def get_memory_usage(self, pid):
        try:
            process = psutil.Process(pid)
            memory_mb = process.memory_info().rss / 1024 / 1024
            memory_info = {
                'rss': memory_mb,
                'vms': process.memory_info().vms / 1024 / 1024,
                'percent': process.memory_percent()
            }
            return memory_info
        except psutil.NoSuchProcess:
            return None

    def setup_dashboard(self):
        self.app.layout = html.Div([
            html.H1('实时进程内存监控'),
            html.Div(id='pid-display', children=f'监控进程PIDs: {", ".join(map(str, self.pids))}'),
            dcc.Graph(id='memory-graph'),
            html.Div(id='memory-stats'),
            dcc.Interval(
                id='interval-component',
                interval=1000 * 2, # 监控间隔
                n_intervals=0
            )
        ])

        @self.app.callback(
            [Output('memory-graph', 'figure'),
             Output('memory-stats', 'children')],
            [Input('interval-component', 'n_intervals')]
        )
        def update_graph(n):
            fig = go.Figure()
            all_stats = []
            
            # 计算子图的行数和列数
            num_pids = len(self.pids)
            cols = min(2, num_pids)  # 最多2列
            rows = (num_pids + 1) // 2  # 向上取整计算行数
            
            fig = make_subplots(rows=rows, cols=cols, 
                              subplot_titles=[f'PID: {pid}' for pid in self.pids])

            for idx, pid in enumerate(self.pids, 1):
                memory_info = self.get_memory_usage(pid)
                if memory_info:
                    current_time = time.time()
                    self.memory_data[pid].append(memory_info['rss'])
                    self.time_data[pid].append(current_time)

                    # 保持固定数量的数据点
                    if len(self.memory_data[pid]) > self.max_points:
                        self.memory_data[pid] = self.memory_data[pid][-self.max_points:]
                        self.time_data[pid] = self.time_data[pid][-self.max_points:]

                    readable_times = [
                        datetime.fromtimestamp(t).strftime('%H:%M:%S')
                        for t in self.time_data[pid]
                    ]

                    row = (idx - 1) // cols + 1
                    col = (idx - 1) % cols + 1

                    fig.add_trace(
                        go.Scatter(
                            x=readable_times,
                            y=self.memory_data[pid],
                            mode='lines+markers',
                            name=f'PID {pid}'
                        ),
                        row=row, col=col
                    )

                    # 更新子图布局
                    fig.update_xaxes(title_text='时间', row=row, col=col, tickangle=45)
                    fig.update_yaxes(title_text='内存 (MB)', row=row, col=col)

                    # 添加统计信息
                    all_stats.extend([
                        html.H3(f'PID: {pid}'),
                        html.P(f"常驻内存(RSS): {memory_info['rss']:.2f} MB"),
                        html.P(f"虚拟内存(VMS): {memory_info['vms']:.2f} MB"),
                        html.P(f"内存占用比: {memory_info['percent']:.2f}%"),
                        html.Hr()
                    ])

            fig.update_layout(
                height=300 * rows,  # 根据行数调整总高度
                showlegend=False,
                title_text="多进程内存使用趋势"
            )

            return fig, all_stats

    def run(self, port=8050):
        print(f"访问 http://localhost:{port} 查看实时监控")
        self.app.run_server(debug=False, port=port)


def find_celery_worker_pids(app_name):
    """查找所有Celery worker的进程ID"""
    try:
        result = subprocess.check_output(
            f"pgrep -f 'celery.*{app_name}'",
            shell=True,
            text=True
        ).strip()
        return [int(pid) for pid in result.split('\n')]  # 返回所有匹配的PID
    except subprocess.CalledProcessError:
        print(f"未找到{app_name} 的Celery worker进程")
        return None


# 使用示例
if __name__ == "__main__":
    # 查找所有匹配的Celery worker PIDs
    pids = find_celery_worker_pids('intelligent_recommend')
    if pids:
        monitor = MemoryMonitor(pids=pids)
        monitor.run()
    else:
        print("未找到进程，请检查Celery worker是否正在运行")
