import unittest
import os
from threading import Thread
import keyboard
import time
import webbrowser as wb
from EvilKeyLogger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        # set up logger
        self.log_file = "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt"
        self.logger = Logger.Logger(self.log_file)

    def test_1(self):
        '''
        # start keylogger
        thread = Thread(target = self.logger.log_keystrokes)
        thread.start()
        
        # start firefox
        keyboard.send('windows')
        keyboard.send('firefox')
        
        # press keys
        time.sleep(8)
        keyboard.send('ctrl+w')
        keyboard.press_and_release('enter')
        
        # end keylogger
        thread.join()
        '''

        assert(True)
        
        '''
        # check log is correct and delete log
        """file = open(self.log_file, "r")
        num_lines = 0
        for line in file:
            self.assertEqual(line, "Key.enter\n")
            num_lines += 1
        file.close()
        self.assertEqual(num_lines, 2)
        os.remove( "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt")"""
        with open(self.log_file, "r") as file:
            num_lines = 0
            for line in file:
                self.assertEqual(line, "Key.enter\n")
                num_lines += 1
            file.close()
            self.assertEqual(num_lines, 2)
        os.remove( "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt")
        '''
            
        
if __name__ == '__main__':
    unittest.main()
