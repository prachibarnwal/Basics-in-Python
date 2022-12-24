def LShift(Arr,n):
    for i in range(n):
        val = Arr.pop(0)
        Arr.append(val)
    print(Arr)

Arr = [10,20,30,40,50,11]
n = int(input("Enter Number of Shifts : "))
LShift(Arr,n)
