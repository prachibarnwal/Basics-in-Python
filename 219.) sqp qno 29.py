def index_list(L):
    r = []
    for i in range(len(L)):
        if L[i] != 0:
            r.append(i)
    return r

L = [12,4,0,11,0,56]
print(index_list(L))
