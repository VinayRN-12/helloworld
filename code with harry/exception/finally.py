try:                                  #  finally always execute if exceptin execute or not
    print("Inside try block")
    x = 10 / 0                        # this will raise ZeroDivisionError
except ZeroDivisionError:
    print("Exception: Division by zero")
finally:
    print("Finally block always runs")


try:
    print("Inside try block")
    x = 10 / 2   # no exception
    print("Result:", x)

except ZeroDivisionError:
    print("Division error")

finally:
    print("Cleanup task done")


    # file handling using exceptin handling

try:
    f = open("example.txt", "w")
    f.write("Hello Vinu!")

except FileNotFoundError:
    print("File not found")
finally:
    f.close()
    f = open("example.txt", "r")
    content=f.read()
    print(content)
    f.close()
    print("File closed safely")

