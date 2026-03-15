# class InsufficientFundsError(Exception):
#     pass

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError("Not enough balance")
#     else:
#         print("Withdraw successful")

# withdraw(500, 1000)


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        message = f"Balance {balance} is not enough to withdraw {amount}"
        super().__init__(message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    else:
        print("Withdraw successful")

try:
    withdraw(500, 1000)
except InsufficientFundsError as e:
    print(" Error:", e)

