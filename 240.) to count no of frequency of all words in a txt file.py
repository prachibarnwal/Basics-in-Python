def findfreq():
    f = open("freq.txt","r")
    data = f.read().split()
    c = {}
    for word in data:
        if word in c:
            c[word] += 1
        else:
            c[word] = 1
    for num in c:
        print(num," occurs ",c[num])

    f.close()

findfreq()

