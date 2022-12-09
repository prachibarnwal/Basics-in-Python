f = open("story.txt","r")
data = f.read()
vowels = 0
cons = 0
lower = 0
upper = 0
for ch in data:
    if ch.isalpha():
        if ch.islower():
            lower += 1
        if ch.isupper():
            upper += 1
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            cons += 1
print("Number of Vowels : ",vowels)
print("Number of Consonants : ",cons)
print("Number of Lower Case : ",lower)
print("Number of Upper Case : ",upper)
f.close()
