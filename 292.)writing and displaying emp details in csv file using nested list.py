import csv
def CREATECSV():
    f=open("EMP2.CSV","w")
    sw=csv.writer(f)
    sw.writerow(['Empno','Empname','Empsalary'])
    lis = []
    for i in range(5):
        Empno=int(input("Enter the employee's number:"))
        Empname=input("Enter the employee's name:")
        Empsalary=float(input("Enter the employee's salary:"))
        lis.append([Empno,Empname,Empsalary])
    sw.writerow(lis)
    f.close()
def DISPLAY():
    f=open("EMP2.CSV","r",newline='\r\n')
    sr=csv.reader(f)
    for r in sr:
        print(r)
    f.close()
CREATECSV()
DISPLAY()
