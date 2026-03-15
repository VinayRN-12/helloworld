# __init__ is a dunder method it is also called constructer
# In Python, a constructor is the __init__() method inside a class.
# It runs automatically whenever you create an object and is used to initialize variables for that object.

# Default Constructor
# A constructor without parameters (except self).
# It sets default values.

class Student:
    def __init__(self):  # Default constructor
        self.name = "Vinu"
        self.age = 21

s1 = Student()
print(s1.name)  # Vinu
print(s1.age)   # 21


# Parameterized Constructor
# A constructor with parameters that takes values when creating an object.

class Student:
    def __init__(self, name, age):  # Parameterized constructor
        self.name = name
        self.age = age

s1 = Student("Vinu", 21)
print(s1.name)  # Vinu
print(s1.age)   # 21
 