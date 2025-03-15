from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_usage_gauge = Gauge('cpu_usage', 'CPU usage percentage')

def collect_metrics():
    """ Функция сбора метрик """
    while True:
        cpu_usage_gauge.set(psutil.cpu_percent(interval=1)) 
        time.sleep(5)

if __name__ == "__main__":
    port = 8000 
    start_http_server(port)
    print(f"Metric exporter running on http://localhost:{port}/metrics")
    collect_metrics()