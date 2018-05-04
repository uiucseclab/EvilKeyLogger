DESCRIPTION:
This is a keylogger for the Windows Desktop platform that parses kestrokes to look for Facebook credentials in the Chrome Web Browser. The software then sends the code to an FTP server, and should uninstall itself from the machine.

SOFTWARE NEEDED:
-Powershell
-Python 3.x (latest version)
-Pip
-Virtualenv
-Various Python modules documented in requirements.txt
-Your choice of FTP server

ABOUT COMPILING:
This software was developed using Powershell (I do not use IDEs). I do not know if it will work in the traditional Windows command line or the newer Linux subsystem. I would advise attempting to compile in Powershell, for that reason. Setting up Powershell for Python development is a bit of a pain, but the following article explains fairly well how it can be done: https://arunrocks.com/guide-to-install-python-or-pip-on-windows/

ABOUT THE FTP SERVER:
I set up the Windows Desktop FTP server for easy testing. Instruction for doing so can be found at the following link: https://www.windowscentral.com/how-set-and-manage-ftp-server-windows-10

COMPILING THE CODE:
1. Download the repo $YOUR-PREFERRED-PATH.
2. Enter `cd $YOUR-PREFERRED-PATH/evilKeyLogger/EvilKeyLogger`.
3. Change the values of log_file and cred_file on lines 9 and 10 of main.py
4. Change the values on line 41 of main.py to their respective values.
5. Create a virtual environment with virtualenv and activate it, using `virtualenv $YOUR-PREFERRED-PATH/venv`, and then `./$YOUR-PREFERRED-PATH/venv/Scripts/activate.ps1`.
6. Run `pip install -r requirements.txt` in $YOUR-PREFERRED-PATH/evilKeyLogger.
7. Run `python setup.py build` in $YOUR-PREFERRED-PATH/evilKeyLogger/EvilKeyLogger.
8. A directory will appear called "build". Use the file explorer to go to $YOUR-PREFERRED-PATH/evilKeyLogger/EvilKeyLogger/build/exe.win32-3.5/, and run "main.exe" as admin.
9. The keylogger is running. Open Chrome, and go to facebook.com
10. Type in both email and password credentials BOTH IN THEIR ENTIRETY.
11. After your login is successful, hit enter. The killer should stop at this point.
12. Check the FTP server. It should have received a file called creds.txt containing a facebook email and password.

WEAKNESSES
1. DOES NOT DELETE ITSELF. This turned out to be a very hard problem, and may not even be possible with Python. There is a sketch of an idea in $YOUR-PREFERRED-PATH/evilKeyLogger/EvilKeyLogger/main.py commented out. It would mark the files for deletion, and delete them upon system restart. Even when run as admin, this code seems to break. This may be easier using a more Windows-centric programming language (C#/VisualBasic/.NET/Powershell).
2. Hard-coding of credentials for the FTP server. It may be better to allow anonymous connections.
3. Browser Functionality. Only works on Chrome. Extending this use to Edge, Firefox, and Opera would be relatively simple. However, Chrome seems to dominates the market and is why I chose to focus on Chrome.
4. Hard-coding of FTP address. I don't know, but I strongly suspect that (like hard-coding credentials) this is a no-no.
5. Cannot parse backspaces.
6. Script won't restart if computer is turned off without user interaction.
7. Does not obfuscate iteslf.
8. Biggest weakness of all: I was not able to integrate my evilChrome.jpg into the program (joking).

FUTURE WORK:
8. I would like to explore getting more credentials (Google, Twitter, etc).
9. I would like to explore adding obfuscation techniques to the compilation process.
