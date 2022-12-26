'''
a binary file emp.dat has the structure (empid,empname,
salary,gender)
- write a function DISPLAY() to read and display the
    contents of emp file
- write a function TRANSFER() to transfer all the
    records from "EMP.dat" to "EMP1.dat", where
    gender is M.
'''
import pickle
import os

def ADD():
    f = open("emp.dat","ab")
    n = int(input("Enter Number of Employees to Add : "))
    for i in range(n):
        emp_id = int(input("Enter Employee Id : "))
        emp_name = input("Enter Employee Name : ")
        salary = int(input("Enter Employee's Salary : "))
        gender = input("Enter Employee's Gender (M/F) : ")
        data = [emp_id,emp_name,salary,gender]
        pickle.dump(data,f)
    print('data saved :")\n')
    f.close()

def DISPLAY():
    f = open("emp.dat","rb")
    try:
        while True:
            data = pickle.load(f)
            print(data)
    except EOFError:
        print("\n")
        f.close()

def TRANSFER():
    f = open("emp.dat","rb")
    g = open("emp1.dat","wb")
    h = open("temp.dat","wb")
    try:
        while True:
            data = pickle.load(f)
            if data[-1].upper() == 'M':
                pickle.dump(data,g)
            else:
                pickle.dump(data,h)
    except EOFError:
        f.close()
        g.close()
        h.close()
        os.remove("emp.dat")
        os.rename("temp.dat","emp.dat")
     
ADD()
DISPLAY()
TRANSFER()
