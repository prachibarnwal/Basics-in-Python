def Copyfile():
    f = open("abc.txt","r")
    g = open("xyz.txt","w")
    data = f.read()
    c = 0
    for ch in data:
        if ch.isalpha() and ch.islower():
            ch = ch.upper()
            c += 1
        g.write(ch)
    f.close()
    g.close()
    print("Total no. of conversions: ",c)


Copyfile()
