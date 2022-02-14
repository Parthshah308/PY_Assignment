"""
Name: Yash parmar
Roll no : 2138
10. Define a function to find a common element between two lists
"""
def common_ele(l1,l2):
   return list(set(l1).intersection(l2))

l1 = [1,2,3,4]
l2 = [2,3,6,7]

com = common_ele(l1,l2)
if len(com) > 0:
    print(com)

else:
    print("no common elements in list")
