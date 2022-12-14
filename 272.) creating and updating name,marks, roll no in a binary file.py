'''
Create a Binary File with Roll Number, Name and Marks. Input a Roll Number and Update the Marks.
'''
import pickle
import os 
while True:
    print("Press 1 - Create the File")
    print("Press 2 - Update a Student's Record")
    print("Press 3 - to Show all Records")
    print("Press 4 - to Exit")
    n = int(input("Enter Your Choice : "))
    if n == 1:
        f = open("Stu.dat","ab")
        s = int(input("Enter Number of Students to add : "))
        for i in range(s):
            rollno = int(input("Enter Roll Number : "))
            name = input("Enter Name : ")
            marks = int(input("Enter Marks : "))
            data = [rollno,name,marks]
            pickle.dump(data,f)
        f.close()
        print("File Created")
    elif n == 2:
        rno = int(input("Enter Roll Number to be Updated : "))
        f = open("Stu.dat","rb")
        g = open("temp.dat","wb")
        found = False
        try:
            while True:
                data = pickle.load(f)
                if data[0] == rno:
                    print("Student ",data[1]," with Roll Number ",data[0]," has Scored ",data[2])
                    marks = int(input("Enter the Modified Marks : "))
                    data[2] = marks
                    found = True
                pickle.dump(data,g)
        except EOFError:
            f.close()
            g.close()
            if found == False:
                print("No Student Found With Given Roll Number")
            else:
                os.remove("Stu.dat")
                os.rename("temp.dat","Stu.dat")
                print("Marks Updated")
    elif n == 3:
        f = open("Stu.dat","rb")
        try:
            while True:
                data = pickle.load(f)
                print("Student ",data[1]," with Roll Number ",data[0]," has Scored ",data[2])
        except EOFError:
            f.close()
    elif n == 4:
        break
    else:
        print("Invalid Choice")
              
