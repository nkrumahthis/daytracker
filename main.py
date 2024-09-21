#! python3

import psutil
import pygetwindow as gw
import time

def get_active_window_title():
    try:
        active_window = gw.getActiveWindow()
        return active_window
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print("daytracker v0.0.0")

    while True:
        current = gw.getActiveWindow()
        print(current)
        time.sleep(5)
