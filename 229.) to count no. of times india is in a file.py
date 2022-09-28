def countindia():
    fl = open("INDIA.txt","r")
    data = fl.read().split()
    c = 0
    for ch in data:
        if ch.lower() == "india":
            c += 1
    print("No. of Word INDIA in The File is : ",c)

countindia()
