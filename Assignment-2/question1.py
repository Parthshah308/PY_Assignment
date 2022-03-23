# 2138 yash parmar
'''
1. Write a program that prompts the user to enter a message. Now count and print the number of
occurrences of each character using a dictionary.
'''
message = input("Enter Message: ")

freq = {} 
    
for ele in message: 
    if ele in freq: 
        freq[ele] += 1
    else: 
        freq[ele] = 1
    
# printing result  
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq)) 