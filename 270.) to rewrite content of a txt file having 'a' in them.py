'''
Remove all the Lines that Contain the Character 'A' in a file and write it to another file.
'''
f = open("story.txt")
g = open("newstory.txt","w")

data = f.readlines()
for line in data:
    if 'a' not in line.lower():
        print(line)
        g.write(line)
g.close()
f.close()
