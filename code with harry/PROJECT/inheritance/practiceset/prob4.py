# add two complex number

class complex():
    def __init__(self,r,i):
     self.r=r
     self.i=i

    def __add__(self,other): #addition 
       return complex(self.r+other.r,self.i+other.i)
    def __mul__(self, other):   # Multiplication
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return complex(real, imag)
    
    def __str__(self):
       return f"{self.r} + {self.i}i"
    
c1=complex(12,7)
c2=complex(7,12)

print(c1+c2)
print(c1*c2)
print((12*12)+(7*7))
