class Employee:
    salary=12000000
    increment=25
    
    @property                                                      
    def salaryAfterIncrement(self):                                        # hear salaryAfterIncrement is a method but in main we are acessing like a attribute
        return self.salary+(self.salary*(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):                       # by using a value from property method we can set the value
        self.increment= (((salary/self.salary)-1)*100)


e=Employee()
newsalary=e.salaryAfterIncrement
print(newsalary)
e.salaryAfterIncrement=20000000
print(e.increment)

