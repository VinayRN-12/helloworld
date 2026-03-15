try:
    num=int(input("Enter a number :"))
    result=10/num
    print(result)

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print("number can't divide by zero")   


print("thankyou")  # Enter a number :0  # number can't divide by zero   # thankyou



try:
    num = int("abc")
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")



# Nested try-except

# We can use try-except inside another try.

try:
    try:
        num = int("abc")
    except ValueError:
        print("Inner block: Invalid number")
    print(10 / 0)
except ZeroDivisionError:
    print("Outer block: Division by zero")


