import csv
def Add():
    f = open("record.csv","a")
    eid = input("Enter Employee id : ")
    name = input("Enter Name : ")
    mobile = input("Enter Employee Mobile Number : ")
    d = [eid,name,mobile]
    cw = csv.writer(f)
    cw.writerow(d)
    f.close()
    print("Employee Added")

def countRec():
    with open("record.csv","r") as f:
        cr = csv.reader(f)
        c = 0
        for data in cr:
            c += 1
        print("No. of Records : ",c)
        
while True:
    Add()
    ans = input("Do You Want to Add More : ")
    if ans.lower() == 'no':
        break
    
countRec()
