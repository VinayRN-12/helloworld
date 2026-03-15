# rename a file 
#   using os module we con delete the file

content="i am old"
with open("old.txt","r") as f:
  content=  f.read()
with open("new .txt","w")as f:
    f.write(content)