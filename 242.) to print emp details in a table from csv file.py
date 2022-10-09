'''Write a program to read above mentioned a CSV file “emp.CSV”
and show data in tabular  form ( without comma).
The program should also show the sum of salary of all employees.
structure [empid, emp_name, salary, mobile_no ]
'''
import csv
f = open("empl.csv")
cr = csv.reader(f)
print("-"*85)
print("EMP_ID","\t|\t","EMP_NAME","|\t","SALARY","\t|\t","MOB_NO.","||")
print("-"*85)
sal  = 0
for row in cr:
    print(row[0],"\t|\t",row[1],"\t|\t",row[2],"\t|\t",row[-1],"||")
    print("-"*85)
    sal += int(row[-2])

print("SUM OF SALARY OF ALL EMPLOYEE : ",sal)
