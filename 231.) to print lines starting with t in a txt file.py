def findlines():
    fl = open("story.txt")
    data = fl.readlines()
    for ch in data:
        if ch[0].lower() == 't':
            print(ch,end = "")
    fl.close()

findlines()
