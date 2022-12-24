def Array_Swap(L):
    a = len(L)
    for i in range(a//2):
        if L[i] % 2 != 0 or (L[a- i - 1]) % 2 != 0:
            L[i],L[a - i - 1] = L[a - i - 1],L[i]
    print(L)
L = list(eval(input("Enter a :ist of Numbers : ")))
Array_Swap(L)
