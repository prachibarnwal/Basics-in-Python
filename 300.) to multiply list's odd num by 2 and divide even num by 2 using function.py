def ODDEVEN(L):
    for ch in L:
        if ch % 2 == 0:
            L[ch] //= 2
        else:
            L[ch] *= 2
    return L

L = list(eval(input("Enter a List Of Numbers : ")))
a = ODDEVEN(L)
print(a)
