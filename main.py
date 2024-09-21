#! python3
import psutil

def get_active_process():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info['name'])

if __name__ == "__main__":
    print("daytracker v0.0.0")

    get_active_process()
