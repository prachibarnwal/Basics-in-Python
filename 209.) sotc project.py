import mysql.connector as sql
import matplotlib.pyplot as plt

mydb = sql.connect(host = "localhost", user = "root", password = "", database = "sotc")

def createcourse(mydb):
    print("🙂🙃"*10)
    cname = input("Enter Course's Name (without spaces and special characters) : ")
    q = "CREATE TABLE "+cname+" (sname varchar(20),doc date,points integer)"
    cr = mydb.cursor()
    cr.execute(q)
    mydb.commit()
    print("🙂🙃"*10)
    print("Course Created........!!!")
    print("🙂🙃"*10)
    pint("\n")


def showpoints():
    print("😇🤩"*10)
    cname = input("Enter Course's Name (without spaces and special characters) : ")
    q = "select sname, sum(points) from " + cname+" group by sname order by sum(points) desc"
    cr = mydb.cursor()
    cr.execute(q)
    res = cr.fetchall()
    names = []
    points = []
    for r in res:
        print(r[0],"\t",r[1])
        names.append(r[0])
        points.append(r[1])
    plt.bar(names,points, color = ['magenta','purple','gray','yellow','red','pink','cyan','green','#99ff99','orange'])
    plt.title(cname + " SOTC CHART")
    plt.show()
    print("😇🤩"*10)    

def showwinners():
    print("🔥😎"*10)
    cname = input("Enter Course's Name (without spaces and special characters) : ")
    q = "select sname, sum(points) from " + cname+" group by sname order by sum(points) desc"
    cr = mydb.cursor()
    cr.execute(q)
    res = cr.fetchmany(5)
    names = []
    points = []
    for r in res:
        print(r[0],"\t",r[1])
        names.append(r[0])
        points.append(r[1])
    plt.bar(names,points, color = ['purple','yellow','pink','green','orange'])
    plt.title("Topper's Name")
    plt.xlabel("Names-->")
    plt.ylabel("Points-->")

    plt.show()
    print("🥳🥳"*10)
    
        

def addpoints():
    print("😄😀"*10)
    cname = input("Enter Course's Name (without spaces and special characters) : ")
    dateofc = input("Enter Date of Class (yyyy-mm-dd) : ")
    for i in range(10):
        sname = input("Enter Student's Name : ")
        points = input("Enter Points : ")
        q = "insert into " +cname+" VAlues(%s,%s,%s)"
        data = [sname,dateofc,points]
        cr = mydb.cursor()
        cr.execute(q,data)
    print("Inserted")
    mydb.commit()
    print("😄😀"*10)



if mydb. is_connected():
    print("Yayyyiiiieeee......Connected......!!!!")

    uname = input("Enter UserName : ")
    pwd = input("Enter Password : ")
    q = "SELECT * FROM USERs WHERE uid = %s and passwrd = %s"
    d = (uname,pwd)
    cr = mydb.cursor()
    cr.execute(q,d)
    res = cr.fetchone()
    n = cr.rowcount
    if n != 1:
        print("Invalid Username and Password")
    else:
        print("* *"*20)
        print("Access Granted.....Welcome.......!!!")
        while True:
            print("* *"*20)
            print("\t\tSOTC MANAGEMENT")
            print("* *"*20)
            print("Press 1 - Create New Course")
            print("Press 2 - Add Points For a Course")
            print("Press 3 - Display Points for a Course")
            print("Press 4 - Show Winners for a Course")
            print("Press 8 - Exit")
            print("* *"*20)
            opt = int(input("Enter Your Choice : "))
            if opt == 1:
                createcourse(mydb)
            elif opt == 2:
                addpoints()
            elif opt == 3:
                showpoints()
            elif opt == 4:
                showwinners()
            elif opt == 8:
                break
        

