'''
Write a function Count() in python to read a
text file "MYFILE.TXT", to copy the content of
file "MYFILE.TXT" inro another file "URFILE.TXT"
by converting capital case character into
small case and vice versa'''

def Count():
    mf = open("MYFILEe.txt")
    uf = open("YOURFILE.txt","w")
    data = mf.read().split()
    for ch in data:
        if ch.islower():
            ch = ch.upper()
        elif ch.isupper():
            ch = ch.lower()
        uf.write(ch)

Count()
