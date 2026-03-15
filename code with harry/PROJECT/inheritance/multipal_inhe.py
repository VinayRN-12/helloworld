# Parent Class 1
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}"

# Parent Class 2
class Coder:
    def code(self):
        return f"{self.name} is coding in {self.language}."

# Child Class (inherits from Employee and Coder)
class Programmer(Employee, Coder):
    def __init__(self, name, role, salary, language):
        # Call Employee constructor to set name, role, salary
        Employee.__init__(self, name, role, salary)
        # Set extra attribute
        self.language = language

# Creating object
p = Programmer("Vinay", "AIML Engineer", 1200000, "Python")

# Using methods from both parents
print(p.get_info())   # From Employee
print(p.code())       # From Coder

