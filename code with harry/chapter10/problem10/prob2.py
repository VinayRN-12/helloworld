import math

class Calculator:
    def __init__(self):
        pass  # No initialization needed now

    def square(self, num):
        result = num * num
        print("Square:", result)

    def cube(self, num):
        result = num * num * num
        print("Cube:", result)

    def root(self, num):
        result = math.sqrt(num)
        print("Square Root:", result)


choice = int(input("Enter 1 for square \n"
                   "Enter 2 for cube \n"
                   "Enter 3 for square root\n"
                   "Enter your choice: "))

num = int(input("Enter a number: "))

c = Calculator()

if choice == 1:
    c.square(num)
elif choice == 2:
    c.cube(num)
elif choice == 3:
    c.root(num)
else:
    print("Invalid choice!")




    import math

class Calculator:
    def __init__(self):
        
        def square(num):
            result = num * num
            print("Square:", result)

        def cube(num):
            result = num * num * num
            print("Cube:", result)

        def root(num):
            result = math.sqrt(num)
            print("Square Root:", result)

        # Store inner functions so we can call them later
        self.square = square
        self.cube = cube
        self.root = root


choice = int(input("Enter 1 for square \n"
                   "Enter 2 for cube \n"
                   "Enter 3 for square root\n"
                   "Enter your choice: "))

num = int(input("Enter a number: "))

c = Calculator()

if choice == 1:
    c.square(num)
elif choice == 2:
    c.cube(num)
elif choice == 3:
    c.root(num)
else:
    print("Invalid choice!")

