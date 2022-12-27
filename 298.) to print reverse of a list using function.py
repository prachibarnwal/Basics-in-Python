#6
def reverse(L):
    a = len(L)
    for i in range(a//2):
        L[i],L[a-i-1] = L[a-i-1],L[i]
    return L

L = list(eval(input("Enter a List Of Numbers : ")))
a = reverse(L)
print(a)
