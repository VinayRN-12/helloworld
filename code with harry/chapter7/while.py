i=1

while(i<10):
    print(i)
    i+=1   # in side while loop

password = ""  # Empty string 
while password != "admin":
    password = input("Enter password: ")

print("Access granted!")  # out side while loop
