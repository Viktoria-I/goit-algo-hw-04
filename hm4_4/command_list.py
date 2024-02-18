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
        return "You don't have any contacts."
        

    for name, phone in contacts.items():
        return f"Your contacts: \n{name}: {phone}\n"


def helper():
    
    return "Available commands:\nadd <name> <phone>: add a new contact\nchange <name> <phone>: change the phone number of a contact\nphone <name>: show the phone number of a contact\nall: show all contacts\nexit or close: close the program"

