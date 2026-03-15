class Employee():    # defining class () inside bracket only parent class is only written

    name="vinay"    # class atributes
    age=23
    salary=1200000
    language="python"
    role="AIML Engineer"  # class attributes

vinay=Employee() # object creation or class initialization
print(f"NAME:{vinay.name}\nAGE:{vinay.age}\nSALARY:{vinay.salary}\nROLE:{vinay.role}")

sanika=Employee()
sanika.name="Sanika S Tuppad"   #  object attributes or instance attribute it belong to that perticular atribute only
sanika.role="HR"               
sanika.salary=1600000
print(f"NAME:{sanika.name}\nAGE:{sanika.age}\nSALARY:{sanika.salary}\nROLE:{sanika.role}")