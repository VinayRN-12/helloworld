class Employee():    # defining class 
    name="vinay"    # class atributes
    age=23
    salary=1200000
    language="python"
    role="AIML Engineer"  # class attributes
    def getinfo(self):
     print(f"NAME:{self.name}\nAGE:{self.age}\nSALARY:{self.salary}\nROLE:{self.role}")


vinay=Employee() # object creation or class initialization
vinay.getinfo()
vinay.getin() # if we don't use self error will come 
