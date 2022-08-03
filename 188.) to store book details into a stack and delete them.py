'''
WAF to add a Book details in a Stack named Library as Push(Library).
Add 5 books in the stack.
Pop and dsplay all the books.
'''
Library = []
def Push(Library):
    name = input("Enter Book Name : ")
    author = input("Enter Author's Name : ")
    date = input("Enter it's Publishing Date (in dd-mm-yyyy format) : ")
    lst = [name, author, date]
    Library.append(lst)
def Pop(Library):
    if len(Library) == 0:
        print("Underflow")
    else:
        a = Library.pop()
        print(a)
for i in range(5):
    Push(Library)
for i in range(5):
    Pop(Library)
        
