# Dictionary is used to store th value based on key

d={} #emptey Dictionary
print(type(d))

dict={"key":"value" ,
      "vinay":"man",
      "sanika":"women",
      "vinay age": "23",
      "sanika age": "23",
      "clas" :[1,2,7]}

print(dict)


student = {
    "name": "Vinu",
    "marks": {
        "math": 90,
        "science": 85
    }
}
print(student)

print(student["marks"]["math"])  #accessing perticular value from nested dictionary using 