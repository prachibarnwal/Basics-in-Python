def EXTRA_ELEMENT(A,B):
    for i in A:
        if i not in B:
            print(i)

A = list(eval(input("Enter a List of Numbers : ")))
B = list(eval(input("Enter a List of Numbers : ")))
EXTRA_ELEMENT(A,B)
