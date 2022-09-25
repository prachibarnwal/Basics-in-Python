import pickle
def add():
    f = open("furdata.dat","ab")
    fid = input("Enter Furniture Id : ")
    fname = input("Enter Name of the Furniture : ")
    fprice = eval(input("Enter Price of the Furniture : "))
    lis = [fid,fname,fprice]
    pickle.dump(lis,f)
    f.close()

def search():
    f = open("furdata.dat","rb")
    try:
        while True:
            cr = pickle.load(f)
            if cr[-1] > 10000:
                print(cr)
    except EOFError:
        f.close()

while True:
    print("Press 1 - to add a furniture detail")
    print("Press 2 - to search ")
    print("Press 3 - to exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        add()
    elif ch == 2:
        search()
    else:
        break
    
