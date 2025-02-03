import psutil
import os
import datetime

class GlobalFix:
    def __init__(self):
        self.task_info = []
    
    def get_task_info(self):
        tasks = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
            try:
                task = {
                    'PID': proc.info['pid'],
                    'Name': proc.info['name'],
                    'User': proc.info['username'],
                    'CPU Usage (%)': proc.info['cpu_percent'],
                    'Memory Usage (MB)': proc.info['memory_info'].rss / (1024 * 1024)
                }
                tasks.append(task)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        self.task_info = tasks

    def display_task_info(self):
        self.get_task_info()
        print("\nCurrent Task Information:")
        for task in self.task_info:
            print(f"PID: {task['PID']}, Name: {task['Name']}, User: {task['User']}, "
                  f"CPU Usage: {task['CPU Usage (%)']}%, Memory Usage: {task['Memory Usage (MB)']} MB")

    def get_system_usage(self):
        system_usage = {
            'CPU Usage (%)': psutil.cpu_percent(interval=1),
            'Total Memory (GB)': psutil.virtual_memory().total / (1024 * 1024 * 1024),
            'Used Memory (GB)': psutil.virtual_memory().used / (1024 * 1024 * 1024),
            'Available Memory (GB)': psutil.virtual_memory().available / (1024 * 1024 * 1024),
            'Disk Usage (%)': psutil.disk_usage('/').percent
        }
        return system_usage

    def display_system_usage(self):
        system_usage = self.get_system_usage()
        print("\nSystem Usage Statistics:")
        for key, value in system_usage.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    global_fix = GlobalFix()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"GlobalFix - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        global_fix.display_task_info()
        global_fix.display_system_usage()
        input("\nPress Enter to refresh...")