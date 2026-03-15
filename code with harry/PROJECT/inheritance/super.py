class vehical:
    def __init__(self):
        print("this is constructure of vehical class")
class car(vehical):
    def __init__(self):
        super().__init__()
        print("this is the constructor of car class")


c1=car()
print(c1)