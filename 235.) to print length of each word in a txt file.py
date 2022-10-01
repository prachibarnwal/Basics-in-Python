def print_length():
    f = open("myfile.txt","r")
    data = f.read().split()
    for ch in data:
        print(len(ch),end = "   ")


print_length()
