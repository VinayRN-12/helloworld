# Function is a block of code which perform specific task

# once write and call many times when ever need

def greet():
    print("hello,vinay")


greet()

# function with parameter 

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)     # Output: 8

print(add(7,12))

# Default Parameter

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
greet("vinay")

# function with multipal return value
def stats(x, y):
    return x + y, x * y

sum_,product = stats(4, 5)
print(sum_,product)   # 9 20
