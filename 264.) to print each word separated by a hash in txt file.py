f = open("story.txt",'r')
data = f.read()
d = data.split()
for i in d:
    print(i,end = "#")

f.close()
