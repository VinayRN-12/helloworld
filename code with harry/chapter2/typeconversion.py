# 🔹 Why Type Casting?
# Because input() gives strings, and we often need numbers or other types to do calculations or comparisons.

# ✅ 1. Implicit Type Casting (Automatic)
# Python does it automatically when it's safe:

a = 5        # int
b = 2.5      # float
c = a + b    # Python automatically makes c a float

print(c)         # 7.5
print(type(c))   # <class 'float'>
# ✅ Python converted int → float to avoid data loss.

# ✅ 2. Explicit Type Casting (Manual)
# You tell Python to convert the type using functions like:

#Function	Converts to
# int()	Integer
# float()	Floating-point
# str()	String
# bool()	Boolean (True/False)

# Example: Convert string to int

x = "20"
y = int(x)    # converts string to int

print(x, type(x))  # "20" <class 'str'>
print(y, type(y))  # 20 <class 'int'>
# Example: Convert float to int

a = 3.9
b = int(a)

print(b)  # 3 (decimal part is removed)
# Example: Convert int to string

num = 100
text = str(num)

print("Number is: " + text)   # Works because both are strings now
# Example: Convert to Boolean

print(bool(0))       # False
print(bool(5))       # True
print(bool(""))      # False
print(bool("Hi"))    # True