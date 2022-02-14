"""
Name : Yash Parmar
Roll no : 2138
12. Consider the list [“OST”, ”WT-II”, “CONM”, “SAD”,”IH”]. Show the output using the comprehensive list.
Output: [“TSO”, ”II-TW”, “MNOC”, “DAS”,”HI”]
"""

mylist = ["OST", "WT-II", "CONM", "SAD","IH"]

newlist = [ele[::-1] for ele in mylist]

print(newlist)