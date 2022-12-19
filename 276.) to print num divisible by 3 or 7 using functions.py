l = list(eval(input("Enter a list of Numbers : ")))
def functionname(L):
    for i in L:
        if i % 3 == 0 or i % 7 == 0:
            print(i, end = "   ")
functionname(l)
