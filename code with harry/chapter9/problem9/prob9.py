# check 2 files are identical 

with open("file.txt")as f:
    content1=f.read()
with open("poem.txt","r")as f:
    content2=f.read()

if (content1==content2):
    print("both files are identical")
else:
    print("both files are not identical")


with open("text.txt")as f:
    content1=f.read()
with open("text_copy.txt","r")as f:
    content2=f.read()

if (content1==content2):
    print("both files are identical")
else:
    print("both files are not identical")