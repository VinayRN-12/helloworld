# strip ad word from list

def fun(l ,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["vinay","sanika","savin","sa"]

print(fun(l,"sa"))