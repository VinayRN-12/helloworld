# celsues to feranat
 
def f_to_c(f):
    c=5*(f-32)/9
    return c

f=int(input("Enter Temperature in faranate:"))
result=f_to_c(f)
print(f"Temperature in celsius:{round(result,1)}c")

