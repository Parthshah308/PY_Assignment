# 2138 Yash Parmar
''' Question 4
Consider a file Bill_Gates.txt and read the content using a readline() and read() method.
'''
try:
    file = open("Bill_Gates.txt","r")
    # using read() method
    print(file.read())
    
    # using readline() method
    print(file.readline())
    file.close()
except:
    print("File not found")