def pattern(n):
    if n==0:
        return # return will do 2 function  1. is return result 2. if condition become true and it terminate function
    print("*"*n)
    pattern(n-1)


pattern(5)


#invers pyramid

def inverted_pyramid(n, i=0):
    # Base condition
    if n == 0:
        return
    
    # Print spaces
    print(" " * i, end="")
    
    # Print stars
    print("*" * (2 * n - 1))
    
    # Recursive call for next row
    inverted_pyramid(n - 1, i + 1)


# Example usage
rows = int(input("Enter number of rows: "))
inverted_pyramid(rows)




def straight_pyramid(n, i=1):
    # Base condition
    if i > n:
        return
    
    # Print spaces
    print(" " * (n - i), end="")
    
    # Print stars
    print("*" * (2 * i - 1))
    
    # Recursive call for next row
    straight_pyramid(n, i + 1)


# Example usage
rows = int(input("Enter number of rows: "))
straight_pyramid(rows)
