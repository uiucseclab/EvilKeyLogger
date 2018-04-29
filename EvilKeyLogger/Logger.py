import sys #
import threading
from win32api import STD_INPUT_HANDLE
from win32console import GetStdHandle, KEY_EVENT, ENABLE_ECHO_INPUT, ENABLE_LINE_INPUT, ENABLE_PROCESSED_INPUT


class Logger():
    def __init__(self):
        self.stopLock = threading.Lock()
        self.stopped = True
        self.capturedChars = ""
        
        self.readHandle = GetStdHandle(STD_INPUT_HANDLE)
        self.readHandle.SetConsoleMode(ENABLE_LINE_INPUT|ENABLE_ECHO_INPUT|ENABLE_PROCESSED_INPUT)
    
    def startReading(self, readCallback):
        self.stopLock.acquire()
        
        try:
            if not self.stopped:
                raise Exception("Capture is already going")
            
            self.stopped = False
            self.readCallback = readCallback
            
            backgroundCaptureThread = threading.Thread(target=self.backgroundThreadReading)
            backgroundCaptureThread.daemon = True
            backgroundCaptureThread.start()
        except:
            self.stopLock.release()
            raise
            
        self.stopLock.release()
    
    def backgroundThreadReading(self):
        curEventLength = 0
        curKeysLength = 0
        while True:
            eventsPeek = self.readHandle.PeekConsoleInput(10000)
            
            self.stopLock.acquire()
            if self.stopped:
                self.stopLock.release()
                return
            self.stopLock.release()
            
            if len(eventsPeek) == 0:
                continue
            
            if not len(eventsPeek) == curEventLength:
                if self.getCharsFromEvents(eventsPeek[curEventLength:]):
                    self.stopLock.acquire()
                    self.stopped = True
                    self.stopLock.release()
                    break
                
                curEventLength = len(eventsPeek)
    
    def getCharsFromEvents(self, eventsPeek):
        callbackReturnedTrue = False
        for curEvent in eventsPeek:
            if curEvent.EventType == KEY_EVENT:
                    print("acc")
                    if ord(curEvent.Char) == 0 or not curEvent.KeyDown:
                        pass
                    else:
                        curChar = str(curEvent.Char)
                        if self.readCallback(curChar) == True:
                            callbackReturnedTrue = True
        
        return callbackReturnedTrue
    
    def stopReading(self):
        self.stopLock.acquire()
        self.stopped = True
        self.stopLock.release()
"""
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
"""
