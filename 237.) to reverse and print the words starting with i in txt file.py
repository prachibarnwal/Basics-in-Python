def reverseText():
    f = open("Country.txt","r")
    d = f.read().split(" ")
    for ch in d:
        if ch[0].lower() == 'i':
            print(ch[::-1],end = " ")
        else:
            print(ch, end = " ")
    f.close()

    
reverseText()
