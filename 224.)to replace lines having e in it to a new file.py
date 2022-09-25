'''Remove all the lines that contain the character 'a' in
        the file and write it in the other file.
'''
f = open("testfile.txt","r")
data = f.readlines()
f.close()

f = open("testfiletxt","w")
for row in data:
    if 'a' in row:
        f.write(row)
f.close()
