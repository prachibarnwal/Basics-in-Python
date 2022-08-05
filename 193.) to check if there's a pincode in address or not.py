n = input("Enter an Address : ")
for i in range(len(n)):
    if n[i].isdigit():
        if n[i:i+6].isdigit():
            print("PinCode in ", n, " is ",n[i:i+6])
            break
