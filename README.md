#Working Terminal 
This script is used to run qterminal and emulate the key presses needed to open 3 tabs and the last tab with split screen.
Afterwards the tabs get renamed to "tun0", "enum" and "attack".
Terminal.sh is intended to be used to run the Python script, which is located at ~/workingTerminal/workingTerminal.py
This program is meant to be run with tmux and also starts tmux logging by itself. 

---
### The second branch is for sessions that don't require TMUX/logging
---
### The python script requires pyautogui, which can be installed via pip:
pip install PyAutoGUI


or in Kali like this:

sudo apt install python3-pyautogui
