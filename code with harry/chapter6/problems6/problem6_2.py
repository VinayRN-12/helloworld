#gretast of four number input taken by user

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))

if a>=b and a>=c and a>=d:
    print("First value is greatest")

elif b>=a and b>=c and b>=d:
    print("Second number is greater")
elif c>=a and c>=b and c>=d:
    print("Third number is greatest")
else:
    print("Fourth number is greatst")

