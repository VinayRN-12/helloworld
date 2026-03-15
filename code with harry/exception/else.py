try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered {num}")     # else won't execute if except run
     
