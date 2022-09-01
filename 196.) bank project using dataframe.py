# Banking Management Project
# Created by : ALCODERS
# FrontEnd : Python
# BackEnd : CSV Files


import pandas as pd
print("🙂🙃"*15)
print("              \t\t\t\tLOGIN             ")
print("🙂🙃"*15)
name  = input("Enter Name : ")
passw = input("Enter Password : ")
df = pd.read_csv("users.csv")
res = df[df["username"] == name]
if res.empty:
    print("😒😒"*15)
    print("\t\t\t\tInvalid Username")
    print("😒😒"*15)
else:
    res = res[res["password"] == passw]
    if res.empty:
        print("😒😒"*15)
        print("Invalid password for given Username")
        print("😒😒"*15)
    else:
        print("\nAccess Granted, Welcome ", name, "..........!!!!!!\n")
if res.empty == False:
    while True:
        print("\n")
        print("😁😁"*15)
        print("              \t\t\t\tAL  BANK             ")
        print("😁😁"*15)
        print("\nPress 1 - Create New Account")
        print("Press 2 -  Display Account Details")
        print("Press 3 - Withdraw Amount")
        print("Press 4 - Deposit Amount")
        print("Press 5 - Display Statement")
        print("Press 6 - Exit\n")
        n = int(input("Enter Your Selected Operation : "))
        if n == 1:
            print("😀😀"*15)
            print("\t\t\t\tENTER DETAILS")
            print("😀😀"*15)
            accno = int(input("Enter Account Number : "))
            name = input("Enter Account Holder Name : ")
            balance = float(input("Enter Initial Amount to Deposit :"))
            phone = input("Enter Phone Number : ")
            dop = input("Enter Today's Date (in dd-mm-yyyy format) : ")
            dt = [accno,name,balance,phone,dop]
            df = pd.read_csv("accounts.csv")
            n = df.shape[0]
            df.loc[n] = dt
            print("🤗🤗"*15)
            print("\t\t\t\tADDED SUCCESSFULLY.....!!!!")
            print("🤗🤗"*15)
            df.to_csv("accounts.csv",index = False)
        elif n == 2:
            print("😀😀"*15)
            print("\t\t\t\tENTER DETAILS")
            print("😀😀"*15)
            accno = int(input("Enter Account Number : "))
            df = pd.read_csv("accounts.csv")
            res = df[df["Accno"] == accno]
            if res.empty:
                print("😣😐"*15)
                print("\tNO DETAILS FOUND WITH THIS ACCOUNT NUMBER")
                print("😣😐"*15)
            else:
                print("😁🤩"*15)
                print("\t\t\t\tMATCH FOUND......!!!!!")
                print("😁🤩"*15)
                print(res)
                print("\n")
        elif n == 3:
            print("😀😀"*15)
            print("\t\t\t\tWITHDRAWING")
            print("😀😀"*15)
            accno = int(input("Enter Account Number : "))
            df = pd.read_csv("accounts.csv")
            for row in df.iterrows():
                if row[1]["Accno"] == accno:
                    print("😁🤩"*15)
                    print("\t\t\t\tMATCH FOUND......!!!!!")
                    print("😁🤩"*15)
                    print(row[1])
                    amount = float(input("Enter the Amount to be Withdrawn : "))
                    dot = input("Enter the Date of Transaction : ")
                    dt = [accno,dot,'Withdraw',amount,"Complete"]
                    if amount > row[1]["Balance"]:
                        print("😣😣"*15)
                        print("Sorry, Insufficient Balance...!!!")
                        print("😣😣"*15)
                        dt[-1] = "Aborted"
                    else:
                        row[1]["Balance"] -= amount
                        df.loc[row[0],"Balance"] = row[1]["Balance"]
                        print("Amount left is ",row[1]["Balance"])
                    tf = pd.read_csv("transact.csv")
                    n = tf.shape[0]
                    tf.loc[n] = dt
                    tf.to_csv("transact.csv", index=False)
                    df.to_csv("accounts.csv", index=False)
                    break
            else:

                print("😖😖" * 15)
                print("No account found with given account number")
                print("😖😖" * 15)

                print("\n")
        elif n == 4:
            print("👌👌" * 15)
            print("                                 DEPOSITING                                                     ")
            print("👌👌" * 15)
            accno = int(input("Enter Account Number : "))
            df = pd.read_csv("accounts.csv")
            for row in df.iterrows():
                if row[1]["Accno"] == accno:

                    print("🥳🥳" * 15)
                    print(
                        "                        MATCH FOUND                                                         ")
                    print("🥳🥳" * 15)
                    print(row[1])
                    amount = float(input("Enter the amount to be deposited "))
                    dot = input("Enter date of transaction ")
                    dt = [accno, dot, 'Deposit', amount, "Complete"]

                    row[1]["Balance"] += amount
                    df.loc[row[0], "Balance"] = row[1]["Balance"]
                    print("Amount updated is ", row[1]["Balance"])
                    tf = pd.read_csv("transact.csv")
                    n = tf.shape[0]
                    tf.loc[n] = dt
                    tf.to_csv("transact.csv", index=False)
                    df.to_csv("accounts.csv", index=False)
                    break
            else:

                print("😖😖" * 15)
                print("No account found with given account number")
                print("😖😖" * 15)

            print("-" * 15)
        elif n == 5:
            print("🙂🙃"*15)
            print("                           ENTER DETAILS                                                            ")
            print("🙂🙃"*15)
            accno = int(input("Enter Account Number : "))
            df = pd.read_csv("transact.csv")
            res = df[df["Accno"] == accno]
            if res.empty:
                print("😖😖"*15)
                print("No account found with given account number")
                print("😖😖"*15)
            else:
                print("🥳🥳"*15)
                print("     MATCH FOUND     ")
                print("🥳🥳"*15)
                print(res)

        elif n == 6:
            print("😊😄"*15)
            print("\t\tTHANKS FOR VISITING.....!!!!)")
            print("😊😄"*15)
            break






            
