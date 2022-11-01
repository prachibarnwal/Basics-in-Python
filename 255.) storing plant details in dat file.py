import pickle
def writeRec():
    f = open("PLANTS.dat","ab")
    pid = input("Enter Plant id : ")
    pname = input("Enter Plant Name : ")
    price = eval(input("Enter Price : "))
    pdata = [pid,pname,price]
    pickle.dump(pdata,f)
    f.close()

def showHigh():
    f = open("PLANTS.dat","rb")
    try:
        while True:
            pdata = pickle.load(f)
            if pdata[2] > 500:
                print(pdata)
    except EOFError:
        f.close()
writeRec()
showHigh()
