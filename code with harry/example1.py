# def add(a,b):
#     ad=a+b
#     print(ad)

# print(add(2,3))

def add(*args):
    return sum(args)

num1=int(input(("Enter a number 1:")))
num2=int(input("Enter a number 2:"))
result=add(num1,num2)
print(result)

