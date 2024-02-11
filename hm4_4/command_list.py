def add_contact(args, contacts):

    if len(args) != 2:
        return "Invalid command."
    name, phone = args

    if name in contacts:
        return "Contact already exists."
    
    try:
        int(phone)
    except ValueError:
        return "Invalid phone number." 
    
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):

    if len(args) != 2:
        return "Invalid command."
    name, phone = args

    if name not in contacts:
        return "Contact not found." 
    
    try:
        int(phone)
    except ValueError:
        return "Invalid phone number." 
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):

    name = args[0]
    
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."
    

def show_all(contacts):

    if not contacts:
        print("You don't have any contacts.")
        print()

    for name, phone in contacts.items():
        print("Your contacts:")
        print(f"{name}: {phone}")
        print()


def helper():
    
    print("Available commands:")
    print("add <name> <phone>: add a new contact")
    print("change <name> <phone>: change the phone number of a contact")
    print("phone <name>: show the phone number of a contact")
    print("all: show all contacts")
    print("exit or close: close the program")
