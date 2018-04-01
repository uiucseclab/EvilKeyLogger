import unittest
import pyautogui
from EvilKeyLogger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        
        # set up logger
        log_file = "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt"
        self.logger = Logger.Logger(log_file)

    def test_1(self):
        pyautogui.press("enter")

    def test_2(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
