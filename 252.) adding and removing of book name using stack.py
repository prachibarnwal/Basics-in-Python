def Addnew(Book):
    while True:
        ch = input("DO YOU WANT TO ADD A BOOK (YES/NO) : ")
        if ch.lower() == "yes":
            bname = input("Enter Book Name : ")
            Book.append(bname)
        else:
            break
def Remove(Book):
    while len(Book) != 0:
        a = Book.pop()
        print(a)
Book = []
Addnew(Book)
Remove(Book)
