from pathlib import Path
from datetime import datetime
import platform
import sys
import psutil

def main():
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")
    
    print("=" * 50)
    print("           SYSTEM INFORMATION")
    print("=" * 50)

    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {sys.version}")
    print(f"Current Working Directory: {Path.cwd()}")
    print("-" * 50)
    
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency (MHz): {psutil.cpu_freq().current}")
    print(f"Total RAM: {round(memory.total / (1024 ** 3), 2)} GB")
    print(f"Available RAM: {round(memory.available / (1024 ** 3), 2)} GB")
    print(f"Used RAM: {round(memory.used / (1024 ** 3), 2)} GB")
    print(f"CPU Usage (%): {psutil.cpu_percent(interval=1)}%")
    print(f"Disk Usage (%): {disk.percent}")
    print(f"Disk Total: {round((disk.total) / (1024 ** 3), 2)} GB")
    print(f"Network Interfaces: {list(psutil.net_if_addrs().keys())}")
    print(f"Network Connections: {len(psutil.net_connections())}")
    print(f"Wifi Status: {'Connected' if psutil.net_if_stats()['Wi-Fi'].isup else 'Disconnected'}")
    print(f"Battery Status: {psutil.sensors_battery().percent if psutil.sensors_battery() else 'No Battery'}%")

    print(f"Generated at: {current_time}")
    
    print("-" * 50)

if __name__ == "__main__":    
    main()
