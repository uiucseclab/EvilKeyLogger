import unittest
import time
import subprocess
from EvilKeyLogger import Identifier

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "C:\\Users\\Benjamin Pollak\\Desktop\\log.txt"
        self.identifier = Identifier.Identifier()

    def test_chrome(self):
        # TODO
        #subprocess.call(['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'])
        proc = subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        time.sleep(2)
        proc.kill()
        assert(True)
        
    def test_edge(self):
        # TODO
        assert(True)
        
    def test_firefox(self):
        # TODO
        #subprocess.call(['C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'])
        proc = subprocess.Popen('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        time.sleep(2)
        proc.kill()
        assert(True)
