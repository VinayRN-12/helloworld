#  # String is sequence of charecters 

# # "Strinng are written in           Single line Comments (single double)      and              Multi line string line(triple quotes) "
# string='''vinay 
# is 
# good boy'''
# print(string)


# string="vinay"

# # String slicing 

# print(string[0:3])  #vin
# print(string[:3])  #vin
# print(string[2:])   #nay

# # String Methods

# # 1 Lower()
# name="VINAY"
# print(name.lower())

# # 2 Upper()
# string="vinay"
# print(string.upper())

# # 3 strip()
# print(string.strip())

# # 4 replace(replacing word,replacing by this word)
# print(string.replace("v","V"))

# # 5 find(sub)
# print(string.find("vi"))


# print("vinay".index("s"))


# nums = [10, 20, 30, 40, 50]
# print(nums[1:4])   # [20, 30, 40]
# print(nums)

# matrix = [[1, 2], [3, 4]]
# print(matrix[1][1])    # 3


# word = "vinu"
# for char in word:
#  result = [char.upper() ]
#  print(result)

string="NAME:{vinay.name}\nAGE:{vinay.age}\nSALARY:{vinay.salary}\nROLE:{vinay.role}"

print(f"{string.replace("vinay","sanika")}")