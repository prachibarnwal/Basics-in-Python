stk = []
def push(stk,ch):
    stk.append(ch)
def pop(stk):
    if len(stk) == 0:
        print("UNDERFLOW")
    else:
        val = stk.pop()
        return val
a = input("Enter a String : ")
for ch in a:
    push(stk,ch)
rev = ""
while len(stk) > 0:
    rev += pop(stk)
if a == rev:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
