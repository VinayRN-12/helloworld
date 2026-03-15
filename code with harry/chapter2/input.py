''' # input() is a in put function which accept input from user 

# Defaultly  input() function takes only string value  

name=input("Enter your name:")
print(name)

# If we want to take different data type from user then user has to type cast 

age=int(input("Enter your age:"))
print(age)

percentage=float(input("Enter your percentage: "))
print(percentage)

# In python we can not type cast string to boolean value
is_student = input("Are you a student? (yes/no): ").lower()
is_student = True if is_student == "yes" else False
print(is_student, type(is_student))


# Method 1: using split (if comma-separated input)
items = input("Enter items separated by commas: ").split(",")
print(items, type(items))  # Output: ['a', 'b', 'c']

# Method 2: using eval (risky, but useful for clean input)
numbers = eval(input("Enter a list (e.g., [1, 2, 3]): "))
print(numbers, type(numbers))  # Output: [1, 2, 3] '''

num=int(input("Enter a number:"))
print(num,type(num))