l = list(eval(input("Enter a List of Names : ")))
def palindrome(L):
    for ch in L:
        if ch == ch[::-1]:
            print(ch)


palindrome(l)
    
