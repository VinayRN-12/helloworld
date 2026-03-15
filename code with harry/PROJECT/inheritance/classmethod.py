class vehical:
    a=1
    def show(self):
        print(f"the value of a is:{self.a}")

class car(vehical):
    def __init__(self):
        print("this is the constructor of car class")


c1=vehical()
c1.a=12
c1.show()  # it will show only object attribute


class vehical:
    a=1
    @classmethod
    def show(cls):
        print(f"the value of a is:{cls.a}")

class car(vehical):
    def __init__(self):
        print("this is the constructor of car class")


c1=vehical()
c1.a=12
c1.show()             # it will show class attribute only because we use @classmethod




class vehical:
    a=1
    @classmethod
    def show(self):
        self.a+=10
        print(f"the value of a is:{self.a}")


c1=vehical()
c1.a=10
c1.show()  
