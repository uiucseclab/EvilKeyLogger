# maybe i dont need this...
import sys
from winpython import wppm, utils

print("a")
dist = wppm.Distribution(sys.prefix)
print("a")
package = wppm.Package(r'C:\Users\Benjamin Pollak\code\evilKeyLogger\EvilKeyLogger\build\exe.win32-3.5\main.exe')
print("a")
dist.install(package)
print("a")
