def SWAP(L):
    n = len(L) 
    if n % 2 == 0:
        gap = n//2
    else:
        gap = n // 2 + 1
    for i in range(n//2):
        L[i], L[i+gap] = L[i+gap],L[i]
    return L
L = list(eval(input("Enter a List of Numbers : ")))
print(SWAP(L))
