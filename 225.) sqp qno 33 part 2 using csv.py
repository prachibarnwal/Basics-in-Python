import csv
def add():
    f = open("furdata.csv","a")
    fid = input("Enter Furniture Id : ")
    fname = input("Enter Name of the Furniture : ")
    fprice = eval(input("Enter Price of the Furniture : "))
    lis = [fid,fname,fprice]
    cw = csv.writer(f)
    cw.writerow(lis)
    f.close()

def search():
    f = open("furdata.csv","r")
    cr = csv.reader(f)
    for rows in cr:
        if int(rows[-1]) > 10000:
            print(rows)
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
    
