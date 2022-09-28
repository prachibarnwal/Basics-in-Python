def rev_text():
    fl = open("data.txt","r")
    data = fl.read().split()
    for ch in data:
        print(ch[::-1], end = " ")
    fl.close()

rev_text()
