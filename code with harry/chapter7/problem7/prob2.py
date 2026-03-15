l=["vinay","sanika","sarvan","aradhya"]

for name in l:
    if(name.startswith("s")):
        print(name)
 # if list consist of ather data type

l = ["vinay", "sanika", "savan", "aradhya", 123, "sameer"]

for name in l:
    if isinstance(name, str) and name.startswith("s"):  # isinstance(name, str)is a built in function What it does It checks if a value (variable) is of a certain type (like str, int, list, etc.).
        print(name)
