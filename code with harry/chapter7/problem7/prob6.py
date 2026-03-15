# factorial of a given number using for loop  5!=5x4x3x2x1

n=int(input("Enter a number which you want:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)


n = 12

# Create the factorial string
factors = []
for i in range(1, n+1, 1):
    factors.append(str(i))

equation = " × ".join(factors)

print(f"{n}! = {equation}")
