LPop = [10,15,20,30]
LPush = []

def PushPop(LPop, LPush,N):
    if len(LPop) < N:
        print("POP NOT POSSIBLE")
    else:
        for i in range(N):
            LPush.append(LPop.pop())

N = int(input("Enter N : "))
PushPop(LPop,LPush,N)
print(LPop)
print(LPush)
