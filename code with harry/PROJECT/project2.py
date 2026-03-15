# from random import randint

# vinay=randint(1,100)
# user= int(input("Enter your prediction: "))
# counter=1

# while(vinay!=user):
#     print("you gess the correct number ",counter)
#     if (vinay>user):
#         print("smaller number please")
#     else:
#         print("larger  number please")
#     counter+=1



from random import randint

vinay = randint(1, 100)  # vinay picks a random number
user = int(input("Enter your prediction (1-100): "))
counter = 1

while vinay != user:
    if vinay > user:
        print("Try a larger number!")
    else:
        print("Try a smaller number!")
    
    counter += 1
    user = int(input("Enter your prediction again: "))

print("🎉 Congratulations! You guessed the correct number in", counter, "tries.")
