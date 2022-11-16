import pickle
import os
found = False
f = open("employ.dat","rb")
g = open("temp.dat","wb")
eid = int(input("Enter The Employee Id To Be Updated : "))
try:
    while True:
        data = pickle.load(f)
        if data[0] == eid:
            print(data)
            found = True
            name = input("Enter Modified Name : ")
            salary = int(input("ENter Modified salary : "))
            data = [eid,name,salary]
            pickle.dump(data,g)
        else:
            pickle.dump(data,g)
except EOFError:
    f.close()
    g.close()
    if found == False:
        print("No Employee Found")
    else:
        os.remove("employ.dat")
        os.rename("temp.dat","employ.dat")
    print("-"*18)
    print("Thankyou")
f.close()
