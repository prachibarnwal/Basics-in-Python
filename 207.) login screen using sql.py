import mysql.connector as sql
mydb = sql.connect(host = "localhost", user = "root", password = "", database = "test")
if mydb. is_connected():
    print("Yayyyiiiieeee......Connected......!!!!")

    uname = input("Enter UserName : ")
    pwd = input("Enter Password : ")
    q = "SELECT * FROM USER WHERE uname = %s and pwd = %s"
    d = (uname,pwd)
    cr = mydb.cursor()
    cr.execute(q,d)
    res = cr.fetchone()
    if res == None:
        print("Invalid Username and Password")
    else:
        print("Access Granted.....Welcome.......!!!")
