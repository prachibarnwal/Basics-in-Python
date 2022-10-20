contacts = {}
while True:
    print("-------------------------------")
    print("Press 1 - Add a New Contact")
    print("Press 2 - Display All Contacts")
    print("Press 3 - Search a Contact")
    print("Press 4 - Delete a Contact")
    print("Press 5 - Upadte a Contact")
    print("Press 6 - Exit")
    print("-------------------------------")
    option = int(input("Enter your choice : "))
    print("-------------------------------")
    if option == 1:
        print("     Adding a New Contact ")
        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")
        contacts[name] = phone
        print("Added")
    elif option == 2:
        print("       Contact List ")
        for n,p in contacts.items():
            print(n, p)
            
    elif option == 3:
        print("          Searching  ")
        name = input("Enter the name to be searched ")
        if name in contacts:
            print("Found, Phone number is ",contacts[name])
        else:
            print("No such name found")
    elif option == 4:
        print("         Deleting  ")
        name = input("Enter the name to be deleted ")
        if name in contacts:
            val = contacts.pop(name)
            print("Current Phone number is ",val)
            
            print(" Deleted Successfully !!!")
        else:
            print("No such name found")
    elif option == 5:
        print("         Updating  ")
        name = input("Enter the name to be updated ")
        if name in contacts:
            print("Current Phone number is ",contacts[name])
            phone = input("Enter new Phone No. ")
            contacts[name] = phone
            print(" Modified Successfully !!!")
        else:
            print("No such name found")
    else:
        break
