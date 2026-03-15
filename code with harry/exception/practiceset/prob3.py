# write a program to write a multiplication table which for user enterd number


num=int(input("Enter a number for which table you want:"))
table=[i*num for i in range(1,11)]
print(table)
    