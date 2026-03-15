# function to write to find greatest of three numbers

def gretest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("number n1 is greatest",n1)
    elif(n2>n1 and n2>n3):
        print("number n2 is greatest",n2)
    else:
        print("number n3 is greatest",n3)

n1=int(input("Enter a n1: "))
n2=int(input("Enter a n2: "))
n3=int(input("Enter a n3: "))

gretest(n1,n2,n3)
  