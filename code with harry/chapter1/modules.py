# # module is python file consist of python code it can be function ,classes ,variables, or runnable code
# # why we use modules
# '''1 organize code properly 
#     2. reuse and reduce code
    
#     types of modules
#     1. Built in modules
#     2. User defined modules
#     3. External module 
#     '''
# # 1 built in module
# import math
# print(math.sqrt(144))

# #import perticular function
# from math import sqrt
# print(sqrt(144))

# #Rename module
# import math as m
# print(m.sqrt(144))



# # 2 User defined module
# import  my_module
# print(my_module.greet("Vinu"))  # Output: Hello, Vinu!


# # 3 External module
# # pip install requests
# import requests

# response = requests.get("https://api.github.com")

# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())


import random

ran_num=random.randint(1, 10)

print(ran_num)


import datetime

now = datetime.datetime.now()
print(now)

#formeted date and time
now = datetime.datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date:", formatted)


# in datetime module there is another class datetime 

from datetime import datetime

now =datetime.now()
print(now)

#formeted date and time
now = datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date:", formatted)
