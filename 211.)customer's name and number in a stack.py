stk = []
def Push(stk):
    cname = input("Enter Customer's Name : ")
    phone = input("Enter Phone Number : ")
    data = [cname,phone]
    stk.append(data)
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
    
n = int(input("Enter how Many Customers are There : "))
for i in range(n):
    Push(stk)
display(stk)
