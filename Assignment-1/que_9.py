"""
Name : Yash parmar
Roll no : 2138
9. Write the function for check palindromes or not.
"""

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        False

n = input("Enter string or number: ")
if (is_palindrome(n)):
    print("Yes it is palindrome")
else:
    print("it is not palindrome")    

## output
## malayalam
## Yes it is palindrome