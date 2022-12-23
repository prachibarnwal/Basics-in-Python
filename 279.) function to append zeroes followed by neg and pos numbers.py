Lis = list(eval(input("Enter A Lsit Of Numbers : ")))
Z = []
N = []
P = []
def receive(Lis):
    for ch in Lis:
        if ch == 0:
            Z.append(ch)
        elif ch < 0:
            N.append(ch)
        else:
            P.append(ch)
    Z.extend(N)
    Z.extend(P)
    return Z

d = receive(Lis)
print(d)
