"""
Name : Yash parmar
Roll no: 2138
5. Take a input from the user. If user entered the input in the lower case then convert into the upper case and
if user enter input into the upper case then convert into the lowercase.
"""

name = input("Enter name : ")

if(name.isupper()):
    print(name.lower())

elif(name.islower()):
    print(name.upper())
    
else:
    print(name)