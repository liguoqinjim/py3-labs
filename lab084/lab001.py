import psutil
import matplotlib.pyplot as plt
import time


def get_celery_memory(pid):
    process = psutil.Process(pid)
    return process.memory_info().rss / (1024 * 1024)  # Convert to MB


def plot_memory_usage(memory_usage):
    plt.plot(memory_usage)
    plt.title('Celery Process Memory Usage')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Usage (MB)')
    plt.show()


def monitor_memory(pid, duration):
    memory_usage = []
    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            memory_usage.append(get_celery_memory(pid))
            time.sleep(1)  # Adjust the interval as needed
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")

    plot_memory_usage(memory_usage)


if __name__ == "__main__":
    celery_pid = int(input("Enter the Celery process PID: "))
    monitor_duration = int(input("Enter the monitoring duration (seconds): "))
    monitor_memory(celery_pid, monitor_duration)
