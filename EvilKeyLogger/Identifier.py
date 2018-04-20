# identify users browser
import wmi
import re

class Identifier:
    def __init__(self):
        self.windows_manager = wmi.WMI()
        self.chrome_regexp = re.compile(r'chrome', re.IGNORECASE)
        self.firefox_regexp = re.compile(r'firefox', re.IGNORECASE)
        self.edge_regexp = re.compile(r'microsoftedge', re.IGNORECASE)
        self.seen_chrome = False
        self.seen_firefox = False
        self.seen_edge = False
    def find_browser(self):
        for proc in self.windows_manager.Win32_process():
            if(self.chrome_regexp.search(proc.Name) and not self.seen_chrome):
                self.seen_chrome = True
                print("chrome")
            if(self.firefox_regexp.search(proc.Name) and not self.seen_firefox):
                self.seen_firefox = True
                print("firefox")
            if(self.edge_regexp.search(proc.Name) and not self.seen_edge):
                self.seen_edge = True
                print("edge")


if __name__ == "__main__":
    id = Identifier()
    id.find_browser()
