#PROGRAM TO FIND WHETHER A NUMBER IS ARMSTRONG OR NOT :)
#  ARMSTRONG NUMBER= it is a number whose sum of cube of its digit is
#                    the number itself.
a = int(input("Enter lower number:"))
b = int(input("Enter upper number:"))
for num in range(a,b+1):
    val = num
    s = 0
    while val > 0:
        d = val % 10
        val //= 10
        s += d**3
    if s == num:
        print(num, "IS ARMSTRONG :)")

    else:
        print(num, "Is NOT ARMSTRONG")
        
