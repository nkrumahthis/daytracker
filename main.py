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

def get_mode(theList):
    counts = {}
    for item in theList:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    max_count = max(counts.values())
    for item in counts:
        if counts[item] == max_count:
            return item


if __name__ == "__main__":
    print("daytracker v0.0.0")
    
    activity = []
    was_doing = []
    
    last_mode_activity = None

    while True:
        sleep_seconds = 15 # TODO: change this sleep value to 5 seconds
        time.sleep(sleep_seconds) 
        
        current = gw.getActiveWindow()
        print(current)
        
        activity.append(current)
        
        ## get the mode activity every ten minutes
        # TODO: change length check to 10 minutes
        if len(activity) == (sleep_seconds * 4 * 10):
            mode_activity = get_mode(activity)
            # print("mode activity: ", mode_activity)
            last_mode_activity = mode_activity
            was_doing.append(mode_activity)
            
            activity = []
