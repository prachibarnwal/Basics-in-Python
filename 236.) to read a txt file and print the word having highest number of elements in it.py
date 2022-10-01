def longestword():
    f = open("story.txt","r")
    d = f.read().split()
    lw = ""
    for word in d:
        if len(word) > len(lw):
            lw = word
    print(lw)
    f.close()

longestword()
