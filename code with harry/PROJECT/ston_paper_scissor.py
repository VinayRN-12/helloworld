# game STON PAPER SCISSOR

import random

'''Ston=1
paper=-1
scissor=0'''

yourchoice=input('''Enter your choice:
                 for stone S
                 for paper P
                 for scissor C:  ''')
yourdic={"s":1,"p":-1,"c":0}
reversdic={1:"stone",-1:"paper",0:"scissor"}

computer=random.choice([1,-1,0])
you=yourdic[yourchoice]
print(f"your choice: {reversdic[you]}  computer choice:{reversdic[computer]}")
if computer==you:
    print("Its is draw")
else:
    if (computer==1 and you==-1):
        print("you win")
    elif (computer==1 and you==0):
        print("computer win")
    elif (computer==-1 and you==1):
        print("computer win")
    elif (computer==-1 and you==0):
        print("you win")
    elif (computer==0 and you==1):
        print("you win")

    elif (computer==0 and you==-1):
        print("computer win")
    else:
        print("Enter a correct choice")