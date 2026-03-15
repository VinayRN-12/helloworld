marks1=int(input("Enter the marks for first subject :"))
marks2=int(input("Enter the marks for second subject"))
marks3=int(input("Enter the marks for third subject"))

total_marks= (100*(marks1+marks2+marks3))/300

if total_marks>=40:
    print("you passed")
    print("congrats")

else:
    print("you failed")
    print("better luck next time")
    