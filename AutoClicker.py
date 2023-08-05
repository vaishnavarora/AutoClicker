# autoclicker.py

import time
import pyautogui as auto

def autoclicker(interval, duration):
    try:
        time.sleep(5)
        auto.write("Now you'll see the power of a coder.")
        auto.press("enter")
        auto.write("Starting spam in 5 seconds. BE READY !!!")
        auto.press("enter")
        print("Autoclicker will start in 5 seconds. Switch to the target window.")
        time.sleep(5)

        end_time = time.time() + duration
        while time.time() < end_time:
            auto.click()
            time.sleep(interval)

        print("Autoclicker has finished.")
    except KeyboardInterrupt:
        print("Autoclicker stopped by the user.")

if __name__ == "__main__":
    click_interval = float(input("Enter click interval (in seconds): "))
    click_duration = int(input("Enter click duration (in seconds): "))
    autoclicker(click_interval, click_duration)
