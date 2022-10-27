'''write definition of a method OddSum(NUMBERS)
        to add those values in the list of numbers,
        which are odd'''
l = []
def OddSum(NUMBERS):
    for i in NUMBERS:
        if i % 2 != 0:
            l.append(i)
    return(l)
NUM = list(eval(input("Enter a List of Numbers : ")))
print(OddSum(NUM))
