'''
WAP to create a stack from a given list of numbers.
Push all those numbers which are divisible by 10 into a stack.
Also write a function to traverse and display a stack if there are any number in the stack.
'''
stack = []
def Push(stack):
    lst = list(eval(input("Enter a list of numbers : ")))
    for ch in lst:
        if ch % 10 == 0:
            stack.append(ch)
def Traverse(stack):
    if len(stack) == 0:
        print("Empty Stack ")
    else:
        for ch in stack:
            print(ch)

while True:
    print("Press 1 - to Push numbers into a stack")
    print("Press 2 - to Traverse the stack")
    print("Press 3 - to Exit")
    ch = int(input("Enter what you want to do : "))
    if ch == 1:
        Push(stack)
    elif ch == 2:
        Traverse(stack)
    else:
        print("program stopped")
        break


    
