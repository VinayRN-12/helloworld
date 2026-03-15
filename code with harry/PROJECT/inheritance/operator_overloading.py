class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __str__(self):
        return str(self.value) 
    
n1=MyNumber(12)
n2=MyNumber(7)
n3=n1+n2
print(n3)
