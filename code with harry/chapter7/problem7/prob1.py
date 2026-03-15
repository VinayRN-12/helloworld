n=int(input("Enter a number which table you want:"))

i=0
for i in range(1,11):
    print(f"{n}X{i}={n*i}      {n}X{11-i}={n*(11-i)}")
    i+=1

    