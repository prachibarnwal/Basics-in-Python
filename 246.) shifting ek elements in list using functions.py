def LShift(Arr,n):
    for i in range(n):
        Arr.append(Arr.pop(0))
        
Arr = [30,40,12,11,10,20]
n = int(input("Enter The Number Of Elements to be Shifted : "))
LShift(Arr,n)
print(Arr)
