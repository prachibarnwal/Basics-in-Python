L = [12,14,0,11,0,56]
indexlist = []
def INDEX_LIST(L):
    for i in range(len(L)):
        if L[i] != 0:
            indexlist.append(i)
    return indexlist

a = INDEX_LIST(L)
print(a)
