#replace word by another word or string

word = input("Enter a word to be censored: ")
replace = "*" * len(word)
print(replace)


with open("file.txt","w") as f:
    f.write("donkey is a donkey donkey has 4 legs donkey is very usefull in work if donkey kicks matash")

with open("file.txt","r") as f:
   print(f.read())  

with open("file.txt","r") as f:
    content=f.read()

newcontent=content.replace(word,replace)

with open("file.txt","w") as f:
    f.write(newcontent)