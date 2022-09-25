import pickle
def Add():
    f = open("record.dat","ab")
    eid = input("Enter Employee id : ")
    name = input("Enter Name : ")
    mobile = input("Enter Employee Mobile Number : ")
    d = [eid,name,mobile]
    pickle.dump(d,f)
    f.close()
    print("Employee Added")

def countRec():
    f = open("record.dat","rb") 
    c = 0
    try:
        while True:
            cr = pickle.load(f)
            c += 1
    except EOFError:
        f.close()
        print("No. of Records : ",c)
        
while True:
    Add()
    ans = input("Do You Want to Add More : ")
    if ans.lower() == 'no':
        break
    
countRec()
