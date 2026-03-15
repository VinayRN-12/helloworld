#search a word in file and print word and line number
word=input("Enter a word to find: ")

with open("log.txt","w")as f:
    f.write("java is a easy programming language \n and it is easy to learn\n python help in aiml,data science data analysis etc is is is isisis ")

with open("log.txt")as f:
     content=f.readlines()
lineno=1
for line in content:
    if(word in line):
       print("yes word present")
       print(f"your word is in line number {lineno}")
       break
    lineno+=1
   
   # The .split() function in Python is used to break a string into a list of smaller strings (called substrings), based on a separator (also called a delimiter).
else:
    print("word not occurd")