# Normally, if you assign a value to a variable inside a function, Python treats it as a local variable.
#  But if you want to change the value of a variable that exists outside the function (in the global scope), 
# you must use the global keyword.


print("with out global keyword")

x = 10  # global variable

def update():
    x = 20  # this creates a new local variable
    print("Inside function:", x)

update()
print("Outside function:", x)


print("with global keyword")
x = 10  # global variable

def update():
    global x
    x = 20  # this creates a new local variable
    print("Inside function:", x)

update()
print("Outside function:", x)
