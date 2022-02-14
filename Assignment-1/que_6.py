"""
Name : Yash Parmar
Roll no : 2138
6.  Make a calculator using function(Addition, subtraction, multiplication, division, square, etc…)
"""
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def square(a):
    return a*a

if __name__ == "__main__":
    
    print("Addition is: {0}".format(add(10,20)))
    print("Subtraction is: {0}".format(sub(20,10)))
    print("Multiplication is: {0}".format(mul(10,20)))
    print("Division is: {0}".format(div(20,5)))
    print("Square root is: {0}".format(square(5)))