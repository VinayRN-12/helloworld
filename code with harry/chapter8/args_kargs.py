# *args lets a function accept any number of positional (normal) arguments.
def add(*args):
    return sum(args)
print(add(12,7,5,10))

def add(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add(12,7,5,10))

# string argument
def greet(*names):
    for name in names:
        print("Hello", name)
greet("Vinu", "Ravi", "Meena")

def show_all(*args):
    for item in args:
        print(item)

show_all("Vinu", "Python", 23)

# What are Positional Arguments in Python?
# 👉 When you call a function and pass values without specifying names, they are called positional arguments.

def greet(name, language):
    print(f"Hello {name}, you are learning {language}!")
greet("Vinu", "Python")
# output: Hello Vinu, you are learning Python!

# If You Change the Order:
greet("Python", "Vinu")
# Hello Python, you are learning Vinu!
# ❌ Wrong meaning! Because positions were changed


# # **kwargs (Keyword)
# Goal: Accept any number of named values

def print_info(**kwargs):        # ← **kwargs = key=value
    for key, value in kwargs.items():
       print(f"{key} → {value}")
print_info(name="Vinu", course="Python", age=22)