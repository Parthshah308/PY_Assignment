"""
Name : Yash parmar
Roll no: 2138
3. Take the message “Welcome to KS school of business management” .
1) FInd out the length of the message.
2) count the character s is how many times come in the message.
3) Consider upper and lower case characters both in counting
"""

message = "Welcome to KS school of business management"

# 1. find length

print("Length of message is {0}".format(len(message)))

# 2. count character s 

#temp variable
temp = message.lower()
print("Character s comes {0} times".format(temp.count('s')))