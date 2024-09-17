contacts = {}

while True:
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. List Contacts")
    print("6. Exit")

    opt = int(input("Enter Your Option: "))

    if opt == 1:
        contact_name = input("Contact Name: ")
        if contact_name in contacts:
            print(f'{contact_name} already exists.')
        else:
            contact_no = input("Contact No: ")
            contacts[contact_name] = contact_no
            print("Contact Added.")

    elif opt == 2:
        contact_name = input("Contact Name to Update: ")
        if contact_name in contacts:
            contact_no = input("New Contact No: ")
            contacts[contact_name] = contact_no
            print("Contact Updated.")
        else:
            print("Contact does not exist.")

    elif opt == 3:
        contact_name = input("Contact Name to Remove: ")
        if contact_name in contacts:
            del contacts[contact_name]
            print("Contact Removed.")
        else:
            print("Contact does not exist.")

    elif opt == 4:
        contact_name = input("Contact Name to Search: ")
        if contact_name in contacts:
            print(f'{contact_name} --------> {contacts[contact_name]}')
        else:
            print("Contact does not exist.")

    elif opt == 5:
        if not contacts:
            print("No contacts available.")
        else:
            for contact_name, contact_no in contacts.items():
                print(f'{contact_name} --------> {contact_no}')

    elif opt == 6:
        print("Exiting...")
        break

    else:
        print("Invalid option, please try again.")
