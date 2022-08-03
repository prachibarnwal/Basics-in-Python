'''
WAF in python Push(Arr) where Arr is a list of numbers.
From this list push all numbers divisible by 5 into a stack implemented list.
Display the sack if it has at least one element.
'''
Arr = list(eval(input("Enter a list of Numbers : ")))
stack = []
def Push(Arr):
    for ch in Arr:
        if ch % 5 == 0:
            stack.append(ch)
    if len(stack) >= 1:
        return stack
print(Push(Arr))
