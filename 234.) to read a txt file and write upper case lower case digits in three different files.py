def copy_data():
    f = open("Main.txt","r")
    u = open("upper.txt","w")
    l = open("lower.txt","w")
    d = open("digits.txt","w")
    data = f.read()
    for ch in data:
        if ch.isdigit():
            d.write(ch)
        elif ch.islower():
            l.write(ch)
        elif ch.isupper():
            u.write(ch)
    f.close()
    u.close()
    l.close()
    d.close()


copy_data()
