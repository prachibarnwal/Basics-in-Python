f = open("testfile.txt","w")
f.write('''Today is a Pleasant Day.
It might rain today.
It is mentioned on weather sites.''')
f.close()

def countET():
    f = open("testfile.txt","r")
    data = f.read()
    e = 0
    t = 0
    for ch in data:
        if ch.lower() =='e':
            e += 1
        elif ch.lower() == 't':
            t += 1
    print("No. of e and E : ",e)
    print("No. of t and T : ",t)

countET()
