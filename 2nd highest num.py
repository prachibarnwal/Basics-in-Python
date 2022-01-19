'''
WAP to find second highest number from a list without using max and sorted
function.
'''
a = eval(input("Enter numbers "))
c = a[0]
for val in a:
    if val > c:
        c = val
c2 = 0
for val in a:
    if val != c and val > c2:
        c2 = val
print("Second highest number is ",c2)

