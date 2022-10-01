a = list(eval(input("Enter a List of Numbers : ")))
n = int(input("Enter the Number of Elements to be Shifted : " ))
print(a)
for i in range(n):
    temp = a.pop(-1)
    a.insert(0,temp)
print(a)
