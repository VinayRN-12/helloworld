''' Inheritance in Python is when one class (child) gets the properties (variables) and behaviors (methods) of another class (parent)
 so you can reuse code instead of rewriting it'''

# Parent Class
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}"

# Child Class (inherits from Employee)
class Programmer(Employee):
    def __init__(self, name, role, salary, language):
        # super() is used to call parent class's constructor
        super().__init__(name, role, salary)
        self.language = language

    def code(self):
        return f"{self.name} is coding in {self.language}."

# Creating an object of the child class
p = Programmer("Vinay", "AIML Engineer", 1200000, "Python")

print(p.get_info())   # method from parent
print(p.code())       # method from child


