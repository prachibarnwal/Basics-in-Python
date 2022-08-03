'''
WAP to use a stack names Company. Define Function Push and Pop to add a
new Employee's name and Salary to the stack and delete an employee respectively.
'''
Company = []
def Push(Company):
    emp = input("Enter Employee's Name : ")
    sal = int(input("Enter Employee's Salary : "))
    lst = [emp, sal]
    Company.append(lst)
def Pop(Company):
    if len(Company) == 0:
        print("Underflow")
    else:
        a = Company.pop()
        print(a)
while True:
    print("Press 1 - to Push an Employee Details")
    print("Press 2 - to Pop an Employee Details")
    print("Press 3 - to Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        Push(Company)
    elif ch == 2:
        Pop(Company)
    else:
        print("PROGRAM FINISHED")
        break
