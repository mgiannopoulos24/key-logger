# Key Logger Program

A key logger program records keystrokes on a computer or device, often for monitoring purposes. Key loggers can be used ethically, such as for employee monitoring or parental control, but they are also frequently misused for malicious purposes like capturing sensitive data, including passwords, credit card numbers, and personal messages.

## Types of Keyloggers
1. **Software Keyloggers:** Capture keystrokes via software that monitors input signals.
2. **Hardware Keyloggers:** Physical devices plugged into a computer or placed between a keyboard and CPU to intercept keystrokes.
3. **Kernel-Based Keyloggers:** Operate at the operating system level, making them harder to detect as they capture input directly from the OS.
4. **Remote Keyloggers:** Usually part of malware, these keyloggers send keystroke data to an attacker remotely.

## How Keyloggers Work
Key loggers intercept input signals from the keyboard to the computer. They save this data either in plain text or encrypted formats. Advanced versions can also detect and record specific sequences, like usernames and password fields, providing a detailed record of user activity.

## Keylogger Techniques in Cyber Attacks
- **Credential Theft:** Capture usernames and passwords for unauthorized access.
- **Surveillance:** Monitor user activities for insights into behavior or habits.
- **Information Gathering:** Collect data that can be used in social engineering attacks or further exploits.

## Features of This Key Logger Program
This key logger includes the following advanced features to enhance data tracking and context:

1. **Application-Specific Logging:** Records the name of the active application each time a key is pressed, providing context on where the input was entered.
2. **Mouse Activity Tracking:** Logs mouse clicks and their screen positions to add context on user interactions.
3. **Clipboard Tracking:** Captures and logs clipboard content periodically, providing a more comprehensive record of user activity.
4. **Screenshot Capture:** Periodically captures screenshots of the screen to provide visual context along with keystrokes.
5. **Periodic Data Backup and Size Monitoring:** Regularly checks log file size and resets it when a set limit is reached, preventing excessive disk usage.
6. **Data Analysis:** Generates visual reports, including keystroke frequency and active application usage, for easy analysis.
7. **Stealth and Obfuscation:** The program operates in the background and includes mechanisms to avoid detection.
8. **Self-Destruct Mechanism:** Monitors log file size and deletes data if it exceeds a set limit to maintain system performance and prevent excessive log buildup.

> **Disclaimer: This key logger program should only be used in environments where monitoring is explicitly authorized and ethical, such as personal device monitoring, parental control, or employee monitoring with consent. Unauthorized use of key loggers is illegal and unethical. Always ensure proper permissions and compliance with legal regulations**.

## Installation
It's recommended to run this key logger program in an isolated environment using Python's virtual environment feature. This keeps dependencies separate and reduces the chance of interfering with system-wide libraries.

## Steps to Set Up and Run in a Virtual Environment
1. Create a Virtual Environment:
```console
python3 -m venv venv
```
2. Activate the Virtual Environment:
- On Windows:
```console
venv\Scripts\activate
```
- On macOS and Linux:
```console
source venv/bin/activate
```
3. Install Dependencies:
With the virtual environment active, install any required packages (e.g., `pynput`, `psutil`, `pillow`, `pandas`, `matplotlib`, `pyperclip`):

For Linux users, first install xclip (required for pyperclip):
```console
sudo apt-get install xclip
```

Then install Python packages:
```console
pip install -r requirements.txt
```
4. Run the Program:
```console
python keylogger.py
```
5. Deactivate the Virtual Environment (when finished):
```console
deactivate
```

> **Note: Running the program in a virtual environment keeps your system environment clean and helps with dependency management.**