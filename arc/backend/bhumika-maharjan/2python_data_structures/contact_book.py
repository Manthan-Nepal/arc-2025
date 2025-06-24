contacts = {}

while True:
    print("Enter 1 to add a contact")
    print("Enter 2 to view contacts")
    print("Enter 3 to search for a contact")
    print("Enter 4 to delete a contact")
    print("Enter 5 to exit")

    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
    
    elif choice == 2:
        if contacts:
            print("The saved contacts are:")
            for name,phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    
    elif choice == 3:
        name = input("Enter the name of the contact to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    
    elif choice == 4:
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} has been deleted.")
        else:
            print("Contact not found.")
    
    elif choice == 5:
        break