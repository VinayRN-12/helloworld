# def withdraw(amount):
#     if amount < 0:
#         raise ValueError("Amount cannot be negative")
#     print("Withdrawing", amount)

# withdraw(-100)



def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    print("Withdrawing", amount)

try:
    withdraw(-100)
except ValueError as E:
    print(" Error:", E)
