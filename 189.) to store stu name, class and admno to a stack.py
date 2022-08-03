'''
WAF AddStudent(student) to add a new student in a stack of students where each
student is represented by student name, adm. no and class.
Also, define RemoveStudent(student) to pop a student from the stack.
'''
student = []
def AddStudent(student):
    name = input("Enter Student Name : ")
    cls = int(input("Enter Class (in digits not in letters) : "))
    admno = int(input("Enter Admission Number : "))
    lst = [name, cls, admno]
    student.append(lst)
def RemoveStudent(student):
    if len(student) == 0:
        print("Underflow")
    else:
        a = student.pop()
        print(a)
while True:
    print("Press 1 - to Add a Student Record")
    print("Press 2 - to Remove a Student Record")
    print("Press 3 - to Exit")
    ch = int(input("ENTER WHAT YOU WANT TO DO : "))
    if ch == 1:
        AddStudent(student)
    elif ch == 2:
        RemoveStudent(student)
    else:
        print("Program finished.")
        break

        




    



    
