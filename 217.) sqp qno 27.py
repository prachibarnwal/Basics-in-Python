f = open("testfile.txt","w")
f.write('''An Apple  day keeps the doctor away.
We all pray for everyone's safety.
A marked difference will come in our country.''')
f.close()

def countlines():
    f = open("testfile.txt","r")
    data = f.readlines()
    c = 0
    for line in data:
        if line[0].lower() not in 'aeiou':
            c += 1
            print(line)
    print("No. of Lines not Starting with a Vowel Are : ",c)

countlines()
