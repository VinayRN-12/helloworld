n=int(input("Enter the number of days: "))
salary=int(input("Enter the salary: "))
for i in range(n):
    salary+=(salary*0.2)

print(f"Final salary: {salary}")
