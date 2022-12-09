N = ['Ankita','Nitish','Anwar','Dimple','Harkirat']
onlyA = []

def Push(N,onlyA):
    for name in N:
        if 'a' in name.lower():
            onlyA.append(name)

def Pop(onlyA):
    while len(onlyA) > 0:
        val = onlyA.pop()
        print(val, end = " " )
    else: print("Empty")

Push(N,onlyA)
Pop(onlyA)
