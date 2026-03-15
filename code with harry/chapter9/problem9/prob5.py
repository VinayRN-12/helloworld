# count the number of times word repted in file
word=input("Enter a word to find: ")

with open("log.txt","w")as f:
    f.write("python is a easy programming language and it is easy to learn python help in aiml,data science data analysis etc is is is isisis ")

with open("log.txt")as f:
    content=f.read()

if(word in content):
    print("yes word present")
    
    count = content.lower().split().count(word.lower())   #ChatGPT said:
    print(f"'{word}' occurs {count} times.")
   # The .split() function in Python is used to break a string into a list of smaller strings (called substrings), based on a separator (also called a delimiter).
else:
    print("word not occurd")