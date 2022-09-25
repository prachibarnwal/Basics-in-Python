status = []
def Push(status,L):
    for data in L:
        if data[2] == 'Goa':
            status.append(data)

def Pop(status):
    if len(status) == 0:
        print("Stack is Empty")
    else:
        print(status.pop())


L = [["Gurdas",'9399329990',"Goa"],["Murugan",'7777777777',"Cochin"],["Julee","8888888888","Mumbai"],["Asmit","849959595","Goa"]]
Push(status,L)

while True:
    Pop(status)
    if len(status) == 0:
        Pop(status)
        break
