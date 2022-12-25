import pickle
def CREATEDICT():
    stu = {"Roll": [], "Name": [], "Class": [], "Section": [], "Marks": []}
    for i in range(2):
        r = int(input("Enter Roll No: "))
        stu["Roll"].append(r)
        n = input("Enter Name: ")
        stu["Name"].append(n)
        c = int(input("Enter Class: "))
        stu["Class"].append(c)
        s = input("Enter Section: ")
        stu["Section"].append(s)
        m = float(input("Enter Marks: "))
        stu["Marks"].append(m)
    with open("Student2.dat", "wb") as f:
        pickle.dump(stu, f)

def DISPLAYDICT():
    rno = int(input("Enter roll no : "))
    with open("Student2.dat", "rb") as f:
        stu = pickle.load(f)
    for i in range(2):
        if stu["Roll"][i] == rno:
            print("Roll No:", stu["Roll"][i])
            print("Name:", stu["Name"][i])


#CREATEDICT()
DISPLAYDICT()
