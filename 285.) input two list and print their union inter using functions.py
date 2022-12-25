'''
Input two lists from user
    write functions named
        Union(A,B)
        Intersection(A,B)
        AminusB(A,B)
        BminusB(A,B)
    and return the result
'''
def Union(A,B):
    res = []
    for i in A:
        res.append(i)
    for i in B:
        if i not in res:
            res.append(i)
    return res

def Inter(A,B):
    res = []
    for ch in A:
        if ch in B:
            res.append(ch)
    return res

def AminusB(A,B):
    res = []
    for ch in A:
        if ch not in B:
            res.append(ch)
    return res

def BminusA(A,B):
    res = []
    for ch in B:
        if ch not in A:
            res.append(ch)
    return res
    
A = list(eval(input("Enter a List of Numbers : ")))
B = list(eval(input("Enter a List of Numbers : ")))
while True:
    print("\n","*"*40)
    print("Press 1 :: for union of two lists")
    print("Press 2 :: for intersection of two lists")
    print("Press 3 :: for A - B")
    print("Press 4 :: for B - A")
    print("Press 5 :: for exit")
    print("*"*40,"\n")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        print(Union(A,B))
    elif ch == 2:
        print(Inter(A,B))
    elif ch == 3:
        print(AminusB(A,B))
    elif ch == 4:
        print(BminusA(A,B))
        
    elif ch == 5:
        break
    else:
        print("5 options me hi choose kro >_____<")
