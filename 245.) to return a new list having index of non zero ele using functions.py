def INDEX_LIST(L):
    indexList = []
    for i in range(len(L)):
        if L[i] != 0:
            indexList.append(i)
    return indexList
L = list(eval(input("Enter a List of Numbers : ")))
print(INDEX_LIST(L))
