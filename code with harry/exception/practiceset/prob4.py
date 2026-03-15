# write a program to divide a/b and throw a error for b=0

try:
     a=int(input("Enter a number:"))
     b=int(input("Enter a number:"))
     result=a/b
     print(result)
except  ZeroDivisionError as e:
     print("Infinate")


    
