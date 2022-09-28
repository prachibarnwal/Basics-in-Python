def JTOI():
    fl = open("words.txt","r")
    data = fl.read()
    for ch in data:
        if ch.upper() == "J":
            print("I",end = "")
        else:
            print(ch,end = "")
    fl.close()
JTOI()
