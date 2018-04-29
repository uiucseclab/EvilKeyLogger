from pynput.keyboard import Key, Listener
import logging

class Logger:
    def __init__(self, log_name):
        self.log_name = log_name
        self.times_enter_pressed = 0
        self.pressed = False
    
    def on_press(self, key):
        myChar = str(key)
        logging.info(str(key))
        return False
        #if(myChar == "Key.enter"):
        #    self.times_enter_pressed+=1
        #    if(self.times_enter_pressed % 2 == 0 and self.times_enter_pressed != 0):
        #        return False
        #else if((myChar == "Key.tab") or self.pressed): # TODO: check
            # TODO: log stuff
	
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.pressed = pressed
        
        
    def log_keystrokes(self):
        logging.basicConfig(filename=(self.log_name), level=logging.DEBUG, format='%(message)s')
        
        with Listener(on_press=self.on_press, on_click = self.on_click) as listener:
            listener.join()
            # return here
