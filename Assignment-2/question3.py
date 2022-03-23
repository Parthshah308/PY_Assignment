# 2138 Yash parmar
'''question 3
Create a file Bill_Gates.txt and write the paragraph using a write() and writeline() and append()
method.

Paragraph: “Bill Gates, in full William Henry Gates III, (born October 28, 1955, Seattle,
Washington, U.S.), American computer programmer and entrepreneur who co founded
Microsoft Corporation, the world's largest personal-computer software company.”
“Gates wrote his first software program at the age of 13. In high school he helped form
a group of programmers who computerized their school's payroll system and founded Traf-O-
Data, a company that sold traffic-counting systems to local governments. In 1975 Gates, then a
sophomore at Harvard University, joined his hometown friend Paul G. Allen to develop software
for the first microcomputers. “
Note:Last sentence write in file by append() method.
'''
para = """Bill Gates, in full William Henry Gates III, (born October 28, 1955, Seattle,
Washington, U.S.), American computer programmer and entrepreneur who co founded
Microsoft Corporation, the world's largest personal-computer software company."""
another_para = """Gates wrote his first software program at the age of 13. In high school he helped form a group of programmers who computerized their school's payroll system and founded Traf-O-
Data, a company that sold traffic-counting systems to local governments. In 1975 Gates, then a
sophomore at Harvard University, joined his hometown friend Paul G. Allen to develop software
for the first microcomputers. """
try:
    file = open("Bill_Gates.txt","w") 
    # file open in write mode
    file.write(para)
    print("Writing some content in file")
    file.close()
    
    file = open("Bill_Gates.txt","a")
    # file open in append mode
    file.write(another_para)
    print("Appending some content in file")
    file.close()
except:
    print("File not found")