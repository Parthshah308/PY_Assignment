#2138 Yash parmar
'''Write a program that combines the lists to a dictionary.
Keys: ['Name','Year','Subject','Marks']
Values: ['yash','SY','OST',45]'''

keys = ['Name','Year','Subject','Marks']
values = ['yash','SY','OST',45]

# empty dictionary
dict = {}

for key in keys:
    for value in values:
        dict[key]=value
        values.remove(value)
        break

print(dict)
