
# file is a data stored in storage device
# a python program can talk to the file by reading content from it and write content to it
file = open("vinu.txt", "w")     # Create or open a file to write
file.write('''Learning Python is fun!
hello vinu how are you 
i am fine''')
file.close()                     # Always close the file


file = open("vinu.txt", "r")     # Open the file in read mode
content = file.read()            # Read what's inside
print(content)                   # Show it on screen
file.close()
