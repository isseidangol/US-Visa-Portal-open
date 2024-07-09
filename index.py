import webbrowser
import time
from datetime import datetime
import pygetwindow as gw
from pywinauto import Application
import pygame

pygame.mixer.init()


def play_sound(file_path):
    print(file_path)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to open the link
def open_link(url, current_hour):
    play_sound('sound.wav')
    webbrowser.open(url)
    print("openned in ", current_hour)
    time.sleep(2)  # Give the browser some time to open
    bring_browser_to_front()

# Function to bring the browser window to the front
def bring_browser_to_front():
    # List of common browser window titles
    browsers = ["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Brave", "Opera"]
    for browser in browsers:
        try:
            # Try to get the window with the browser's title
            window = gw.getWindowsWithTitle(browser)[0]
            window.activate()  # Bring the window to the front
            break
        except IndexError:
            continue

# Function to check the current time and open the link at specified times
def schedule_link_opening(url):
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_second = now.second
        if current_hour % 2 == 0:  # Even hour
            if current_minute == 10 and current_second == 45:
                open_link(url,current_hour)
                time.sleep(61)  # Wait 61 seconds to avoid multiple openings in the same minute
        else:  # Odd hour
            if current_minute == 2 and current_second == 45:
                open_link(url, current_hour)
                time.sleep(61)  # Wait 61 seconds to avoid multiple openings in the same minute

        time.sleep(1)  # Check the time every second

# Specify the URL to open
url = "https://portal.ustraveldocs.com/"

# Start the scheduling
schedule_link_opening(url)
# open_link(url,1)
