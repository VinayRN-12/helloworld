# write a program to make a copy of the text file
content=" i love you python \n i will learn you fast and correctly \n with in two months i will become a AIML engineer"
with open("text.txt","w") as f:
    f.write(content)

with open("text.txt")as f:
    copy=f.read()

with open("text_copy.txt","w")as f:
    f.write(copy)