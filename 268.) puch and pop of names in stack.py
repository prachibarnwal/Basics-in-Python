'''
Write Functions in Python for Insert(Names)
    and for Remove(Names) for performing insertion
        and removal operations with a stack of List
            which contains names of students.
'''
Names = ['Prachi','Anjali','Jiya','Ash','Apoorva','Sameer','Navneet','Aziz','Harshit']

def Insert(Names):
    n = input("Enter a Name to Push : ")
    Names.append(n)

def Remove(Names):
    if len(Names) == 0:
        print("UNDERFLOW - stack is empty")
    else:
        a = Names.pop()
        print(a)

while True:
    print("\nPress 1 - to Insert a Name")
    print("Press 2 - to Remove a Name")
    print("Press 3 - to Show all Names")
    print("Press 4 - to Exit")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        Insert(Names)
    elif ch == 2:
        Remove(Names)
    elif ch == 3:
        for ch in Names:
            print(ch, end = "   ")
    elif ch == 4:
        break
    else:
        print("5 Options hi the -_-")
