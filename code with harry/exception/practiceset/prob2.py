# write a program to write a enumerate function to find  3rd 4th and 7th value from list

l=[1,2,3,4,5,6,7,8,9,10]

for index,item in enumerate(l):
    if (index==3 or index==4 or index==7):
        print(index,item)


#  with start index 1

l=[1,2,3,4,5,6,7,8,9,10]

for index,item in enumerate(l,start=1):
    if (index==3 or index==4 or index==7):
        print(index,item)
