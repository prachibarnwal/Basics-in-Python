def DIVISIBLE(L):
    s = 0
    for ch in L:
        if ch % 3 == 0 or ch % 5 == 0:
            s += ch
    print(s)

L = list(eval(input("ENTER A LIST OF NUMBERS : ")))
DIVISIBLE(L)
