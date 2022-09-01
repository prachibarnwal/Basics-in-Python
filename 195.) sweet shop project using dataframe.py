import pandas as pd


def addsweets():
    scode = int(input("Enter the Sweet's code : "))
    sname = input("Enter the Sweet Name : ")
    ppp = int(input("Enter Sweet's Price per Piece : "))
    ppk = int(input("Enter Sweet's Price per Kilo : "))
    qty = float(input("Enter quantity in kgs : "))
    ig = input("Enter the main ingredient : ")
    df.loc[scode] = [sname, ppp, ppk, qty, ig]
    print("\nAdded Successfully\n")

def showsweets():
    print("\n", "*"*60)
    print(df)
    print("*"*60)

def searchsweet():
    code = int(input("Enter the sweet code to be searched : "))
    if code in df.index:
        print("\nSweet Details Found....!!!\n")
        print(df.loc[code],"\n")
    else:
        print("\nNo Sweet Found with this Code.\n")

def delsweets():
    code = int(input("Enter the sweet code to be deleted : "))
    if code in df.index:
        df.drop(code, inplace = True)
        print("\nSweet with code ", code, " DELETED\n")
    else:
        print("\nNo Sweet Found with this Code.\n")

def updatesweets():
    global sname, ppp, ppk, qty, ig
    ppp = 0
    ppk = 0
    qty = 0
    ig = 0
    code = int(input("Enter the sweet code to be updated : "))
    if code in df.index:
        sname = df.at[code,"Name"]
        ppp = df.at[code,"Costp"]
        ppk = df.at[code, "Costk"]
        qty = df.at[code, "Quantity"]
        ig = df.at[code, "Ingredient"]
        print("Current Values are ")
        print(df.loc[code,:])
        while True:
            print("Press 1 - to Update Name")
            print("Press 2 - to update price per piece")
            print("Press 3 - to update price per kilo")
            print("Press 4 - to update quantity of the sweet")
            print("Press 5 - to update ingredients of the sweet")
            print("Press 6 - to go to the main menu")
            n = int(input("Enter your Choice : "))
            if n == 1:
                sname = input("Enter the New Sweet Name to be Updated : ")
                df.loc[code] = [sname, ppp, ppk,qty,ig]
                print("\nUPDATED....!!!\n")
            elif n == 2:
                ppp = int(input("Enter the New Sweet's Price per Piece to be Updated : "))
                df.loc[code] = [sname,ppp,ppk,qty,ig]
                print("\nUPDATED....!!!\n")
            elif n == 3:
                ppk = int(input("Enter the New Sweet's Price per Kilo to be Updated : "))
                df.loc[code] = [sname, ppp, ppk,qty,ig]
                print("\nUPDATED....!!!\n")
            elif n == 4:
                qty = int(input("Enter the New Quantity of Sweet to be Updated : "))
                df.loc[code] = [sname, ppp, ppk,qty,ig]
                print("\nUPDATED....!!!\n")
            elif n == 5:
                ig = input("Enter the New Sweet's Ingredients to be Updated : ")
                df.loc[code] = [sname, ppp, ppk,qty,ig]
                print("\nUPDATED....!!!\n")
            else:
                print("\n")
                break
    else:
        print("\nNo Sweet Found with this Code.\n")


print("*"*60)
print("\t**** ALCODER'S SWEET SHOP****")
print("*"*60)
df = pd.read_csv("Sweets.csv")

while True:
    print("Press 1 - to add Record of a New Sweet")
    print("Press 2 - to delete Record of an Existing Sweet")
    print("Press 3 - to show All Sweets")
    print("Press 4 - to Search a Sweet")
    print("Press 5 - to Update a Sweet's Record")
    print("Press 6 - to Exit the Shop")
    print("-"*60)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        addsweets()
    elif ch == 2:
        delsweets()
    elif ch == 3:
        showsweets()
    elif ch == 4:
        searchsweet()
    elif ch == 5:
        updatesweets()
    elif ch == 6:
        df.to_csv("sweets.csv", index  = False)
        print("Thanks for Visiting the Shop")
        print("\nData Updated....!!!!!\n")
        break
    else:
        print("\nYOU'RE GIVEN ONLY 4 CHOICES -___-\n")



