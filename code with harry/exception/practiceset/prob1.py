# Create the 3 files if any of the file is not exist then throw the error
try:
     with open("text1.txt")as f:
        print(f.read())
except Exception as e:
        print(e)
try:
    with open("text2.txt")as f:
         print(f.read())
except Exception as e:
         print(e)
try:
    with open("text3.txt")as f:
         print(f.read())
except Exception as e:
        print(e)

print("thank you")  # program not exiting it is throwing error