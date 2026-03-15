file=open("poem.txt","w")
file.write("vinay is a bod boy \n he dont obay any ones word")
file.close()

file=open("poem.txt")  # these line of code help in read fiel 
print(file.read())
file.close()

file=open("poem.txt")  # this line of code help in checking perticular word in the text file

c=file.read()
if("word" in c):
    print("vinay is there in the file")
else:
    print("vinay is not there in the file")


file=open("poem.txt")  # this line of code help in checking perticular word in the text file

c1=file.readlines()
c2=file.readlines()

if("word" in c1,c2):
    print("vinay is there in the file")
else:
    print("vinay is not there in the file")



