def ODDLIST(a):
    if len(a) % 2 == 0:
        print("ENTER A LIST WITH ODD NUM OF ELEMENTS")
    else:
        a = len(a) // 2
        print(L[a])

L = list(eval(input("Enter a List of Numbers : ")))
ODDLIST(L)
