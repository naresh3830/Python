import psutil
import time

def monitor_cpu(threshold=80):
    try:
        print("Monitoring CPU usage...")
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")
            
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {threshold}%")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Monitoring interrupted. Exiting...")

if __name__ == "__main__":
    try:
        monitor_cpu()

    except Exception as e:
        print(f"An error occurred: {e}")
