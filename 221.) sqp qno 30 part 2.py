sitem = []
def Push(sitem,D):
    for k in D:
        if D[k] > 75:
            sitem.append(k)

Ditem = {"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}
Push(sitem,Ditem)

print("NO. of elements is stack : ",len(sitem))

