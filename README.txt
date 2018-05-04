
DESCRIPTION:
This is a keylogger for the Windows Desktop platform that parses kestrokes to look for Facebook credentials in the Chrome Web Browser. The software then sends the code to an FTP server, and uninstalls itself from the machine.

I set up the Windows Desktop FTP server. Instruction for doing so can be found at the following link: https://www.windowscentral.com/how-set-and-manage-ftp-server-windows-10

SOFTWARE NEEDED:
-Powershell
-Python 3.x (latest version)
-Pip
-Virtualenv
-Various Python modules documented in requirements.txt
-Your choice of FTP server

ABOUT COMPILING:
This software was developed using Powershell (I do not use IDEs). I do not know if it will work in the traditional Windows command line or the newer Linux subsystem. I would advise attempting to compile in Powershell, for that reason. Setting up Powershell for Python development is a bit of a pain, but the following article explains fairly well how it can be done: https://arunrocks.com/guide-to-install-python-or-pip-on-windows/

COMPILING THE CODE:
1. Download the repo $YOUR-PREFERRED-PATH.
2. Enter `cd $YOUR-PREFERRED-PATH/evilKeyLogger/EvilKeyLogger`.
3. Change the values of log_file and cred_file on lines 9 and 10 of main.py
4. Change the values on line 41 of main.py to their respective values.
5. Create a virtual environment with virtualenv and activate it.
6. Run `pip install -r requirements.txt`.
7. Run `python setup.py build`.
8.

SEEING THAT IT WORKS:
1.

WEAKNESSES AND FUTURE WORK:
1. Hard-coding of credentials for the FTP server. It may be better to allow anonymous connections.
2. Browser Functionality. Only works on Chrome. Extending this use to Edge, Firefox, and Opera would be relatively simple. However, Chrome seems to dominates the market and is why I chose to focus on Chrome.
3. Hard-coding of FTP address. I don't know, but I strongly suspect that (like hard-coding credentials) this is a no-no.
4. I would like to explore getting more credentials (Google, Twitter, etc).
