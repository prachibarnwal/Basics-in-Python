import pickle
def SEARCH(sid):
    f = open("STUDENT.dat",'rb')
    try:
        while True:
            data = pickle.load(f)
            if data[0] == sid:
                print(data)
    except:
        f.close()

def DISPLAY():
    f = open("STUDENT.dat",'rb')
    c = 0
    try:
        while True:
            data = pickle.load(f)
            if data[-1] > 90:
                c += 1
                print(data)
        print(c)
    except:
        f.close()

def ADD():
    f = open("STUDENT.dat","ab")
    sid = int(input("Enter Student id : "))
    sname = input("Enter Studnet's Name : ")
    marks = int(input("Enter Marks : "))
    data = (sid,sname,marks)
    pickle.dump(data,f)
    f.close()

while True:
    print("1 -- to add")
    print("2 -- to display all")
    print("3 -- to search")
    print("4 -- to exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        ADD()
    elif ch == 2:
        DISPLAY()
    elif ch == 3:
        sid = int(input("Enter id of the student to be searched : "))
        SEARCH(sid)
    else:
        break

                
    
