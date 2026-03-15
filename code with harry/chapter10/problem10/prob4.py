from random import randint

class train:
    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo
        self.fro=fro
        self.to=to
    def book(self):
        print(f"Ticket is Booked in train no:{self.trainNo}  from {self.fro} to {self.to}")
    def getstatus(self):
        print(f"Train no:{self.trainNo} is running on time")
    def getfare(self):
        print(f"Ticket fare in train no :{self.trainNo} from {self.fro} to{self.to} is {randint(222,3333)}")

t=train(12719, "chitradurga","bangloure")
t.book()
t.getstatus()
t.getfare()