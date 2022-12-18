OnlyA = []
N = ["Kartik","Navneet","Lucky","Esha","Anvesha","Harsh","Nitin","Dev"]
def Push(N,OnlyA):
    for name in N:
        if 'A' in name or 'a' in name:
            OnlyA.append(name)

def Pop(OnlyA):
    while True:
        if len(OnlyA) == 0:
            print("EMPTY", end = " ")
            break
        else:
            print(OnlyA.pop(), end = " ")
            
Push(N,OnlyA)
Pop(OnlyA)
