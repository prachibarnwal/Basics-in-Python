'''
Create a Binary File with Name and Roll Number. Search for a Given Roll Number and Display the Name, if nit fiund display appropriate message.
'''
import pickle
while True:
    print("Press 1 - Create the File")
    print("Press 2 - Search a Student")
    print("Press 3 - to Exit")
    n = int(input("Enter Your Choice : "))
    if n == 1:
        f = open("Student.dat","ab")
        s = int(input("Enter Number of Students to add : "))
        for i in range(s):
            rollno = int(input("Enter Roll Number : "))
            name = input("Enter Name : ")
            data = [rollno,name]
            pickle.dump(data,f)
        f.close()
        print("File Created")
    elif n == 2:
        rno = int(input("Enter Roll Number to be Searched : "))
        f = open("Student.dat","rb")
        found = False
        try:
            while True:
                data = pickle.load(f)
                if data[0] == rno:
                    print("Found Name is : ",data[1])
                    found = True
                    break
        except EOFError:
            f.close()
            if found == False:
                print("No Student Found With Given Roll Number")
    elif n == 3:
        break
    else:
        print("Invalid Choice")
              
