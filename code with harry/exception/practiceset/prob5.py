# generate a tables

num=int(input("Enter a number for which table you want:"))
table=[i*num for i in range(1,11)]
with open("table.txt","a")as f:
    f.write(f"Table of {num}:{str(table)}\n ")

