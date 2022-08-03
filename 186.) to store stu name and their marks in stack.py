'''
WAP in python to create a stack Student with details of student name and their marks.
Write Push Pop and Traversal operation using menu.
'''
Student = []
def Push(Student):
    name = input("Enter Student's Name : ")
    marks = eval(input("Enter Marks : "))
    st = [name,marks]
    Student.append(st)
def Pop(Student):
    if len(Student) == 0:
        print("Underflow")
    else:
        p = Student.pop()
        print(p)
def Traversal(Student):
    if len(Student) == 0:
        print("First put some info to the stack then only you'll be able to see the records :)")
    else:
        for ch in Student:
            print(ch)
while True:
    print("Press 1 - to Push a Record")
    print("Press 2 - to Pop a Record")
    print("Press 3 - to See All the Records")
    print("Press 4 - to Exit")
    a = int(input("Enter your choice : "))
    if a == 1:
        Push(Student)
    elif a == 2:
        Pop(Student)
    elif a == 3:
        Traversal(Student)
    elif a == 4:
        print("Program Finished")
        break
    else:
        print("You had only 4 options to choose -__-")
