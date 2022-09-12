r = {"Om" : 85,"John" : 65,"Bob" : 78,"Jerry" : 98,"Tom" : 72}
stk = []
def Push(stk,r):
    for k in r:
        if r[k] > 75:
            stk.append(k)

def Pop(stk):
    while len(stk) > 0:
        print(stk.pop(), end = ' ')
        
Push(stk,r)
Pop(stk)
