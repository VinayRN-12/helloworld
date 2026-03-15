# f=open("vinu.txt","r")# file always open in read mode when we want to write the file then we should mention mode
# lines=f.readlines()
# print(lines,type(lines))  # readlines() function used to print multipal line ata time 
# f.close() # this readlines() function provide data in list data type

   


# line1=f.readline()            # these readline() function print individual line in file 
# print(line1,type(line1))
# line2=f.readline()               # these provide data type in string
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# line4=f.readline()
# print(line4,type(line4))

# # READ MULTIPAL LINE USING WHILE LOOP
# f=open("vinu.txt","r")
# line=f.readlines()
# word="vinu"
# while(word in line):
#    print(line)
# f.close()
# with open("data.txt","w")as f:
#     f.write("vinay how are you " \
#     "i am fine" \
#     "how you are ")
# f = open("data.txt", "r")
# print(f.read(10))       # read first 10 chars
# print("Position:", f.tell())
# f.seek(0)               # reset to start   @ with out this f.seek(0) vinay how/ Position: 10 / are y
# print("Position:", f.tell())
# print(f.read(5))
# f.close()



with open("copy.jpg", "wb") as f:
    f.write("data")
with open("image.jpg", "rb") as f:
    data = f.read()


