def display_menu():
    print("\n--- MENU ---")
    print("1. Add contact")
    print("2. View Contact")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted.")
    else:
        print("Contact not found.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
