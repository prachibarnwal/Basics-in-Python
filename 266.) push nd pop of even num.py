N = [10,5,3,8,15,14]
even = []

def Push(N,even):
    for name in N:
        if name % 2 ==0:
            even.append(name)

def Pop(even):
    while len(even) > 0:
        val = even.pop()
        print(val, end = " " )
    
Push(N,even)
Pop(even)
