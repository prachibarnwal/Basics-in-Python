a = eval(input("Enter First Number : "))
b = eval(input("Enter Second Number : "))
c = eval(input("Enter Third Number : "))
if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
elif c > b and c > a:
    if a > b:
        print(a)
    else:
        print(b)
