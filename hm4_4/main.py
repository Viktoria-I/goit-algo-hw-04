from command_list import add_contact, change_contact, show_phone, show_all, helper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot! To get the list of commands, type 'help'.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            print()
            break
        elif command == "hello":
            print("How can I help you?")
            print()
        elif command == "help":
            helper()
            print()
        elif command == "add":
            print(add_contact(args, contacts))
            print()
        elif command == "change":
            print(change_contact(args, contacts))
            print()
        elif command == "phone":
            print(show_phone(args, contacts))
            print()
        elif command == "all":
            show_all(contacts)
            print()
        else:
            print("Invalid command.")
            print()

if __name__ == "__main__":
    main()