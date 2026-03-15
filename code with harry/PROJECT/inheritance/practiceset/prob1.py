# creat a class 2dvector and creat another vector 3dvector from 2d vector

class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
     print(f"The two D vector: {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
      print(f"The two D vector: {self.i}i + {self.j}j + {self.k}k")

D2=TwoDvector(1,2)
D2.show()
D2=ThreeDvector(1,2,3)
D2.show()