def Fib(n):
    t = (0,1)
    for i in range(2,n):
        num = t[i-1] + t[i-2]
        t += (num,)
    return t

n = int(input("Enter the Number of Elements Required in Fibonacci Series : "))
res = Fib(n)
print(res)
