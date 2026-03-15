p1="make lot of money"
p2="click to subscribe"
p3="enter your detailes"

message=input("Enter your message")

if((p1 in message)or(p2 in message)or(p3 in message)):
    print("Enterd comment is spam")
else:
    print("Enterd comment is not spam")
    