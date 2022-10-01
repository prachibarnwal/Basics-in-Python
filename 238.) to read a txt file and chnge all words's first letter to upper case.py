def convert_case():
    f = open("Movie.txt")
    d = f.read().split()
    for ch in d:
        print(ch.capitalize(),end = " ")
    f.close()

convert_case()
