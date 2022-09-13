r = [10,39,50,28,47,40,50,38,50,20,58,39,67,89]
stk = []
def Push(stk,r):
    for k in r:
        if k % 2 == 0:
            stk.append(k)

def Pop(stk):
    if len(stk) > 0:
        print(stk.pop(), end = ' ')
    else:
        print("Underflow")
def display(stk):
    for i in range(len(stk) - 1, -1, -1):
        print(stk[i])
def Peep(stk):
    return stk[-1]
    
Push(stk,r)
display(stk)
