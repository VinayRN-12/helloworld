# write a function to sum first n natural numbers

def fs_su(n):
    sum=0
    for i in range(1,n+1):
         sum+=i
    return sum

num=int(input("Enter a number :"))
result=fs_su(num)
print(f"Sum of first {num} natural number:{result}")

#using recursion

def sum(n):
     if n==1:
          return 1
     return sum(n-1)+n

num=int(input("Enter a number :"))
result=sum(num)
print(f"Sum of first {num} natural number:{result}")