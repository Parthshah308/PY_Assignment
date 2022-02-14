"""
Name : Yash Parmar
Roll no : 2138
15. Write a program that prompts the user to enter a number. If the number is positive and zero print it,
otherwise raise an exception.
"""
if __name__ == "__main__":
    try:
        num = int(input("Enter number: "))
        if(num > 0 or num == 0):
            print(num) 
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input")
