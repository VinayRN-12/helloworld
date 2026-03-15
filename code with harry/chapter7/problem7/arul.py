# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(" "* (n - i), end="")        # spaces
#     print("*"* (2 * i - 1), end="")    # stars
#     print()

# n = int(input("Enter number of rows: "))

# for i in range(n, 0, -1):
#     print(i)
#     print(" " * (n - i), end="")       # spaces
#     print("*" * (2 * i - 1), end="")   # stars
#     print()
# n = int(input("Enter number of rows: "))
# for i in range(0, n+2, 2):
#      print(i)

n=int(input("Enter the number of rows:"))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print()
        
# n = int(input("Enter the number of rows:"))  # Takes input for the number of rows (and columns, since it's a square)

# for i in range(1, n + 1):  # Loop through 1 to n
#     if i == 1 or i == n:  # For the first and last row
#         print("*" * n, end="")  # Print all '*'
#     else:
#         print("*", end="")             # Start of row
#         print(" " * (n - 2), end="")   # Middle spaces
#         print("*", end="")             # End of row
#     print()  # Move to the next line

    




    