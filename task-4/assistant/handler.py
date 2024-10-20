# handling errors through decorators
def input_error(func):
    def inner(*args, **kwars):
        try:
            return func(*args, **kwars)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Please, enter the correct arguments for the command."

    return inner


@input_error
def parse_input(user_input: str) -> tuple[str, list]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    operation_type = "added"

    if name in contacts:
        operation_type = "updated"

        # verify if contact is exists and waiting the answer if it is necessary
        while True:
            user_input = (
                input("Contact is exists, overwrite it(yes=default,no)? ") or "yes"
            )
            command, *args = parse_input(user_input)

            if command == "no":
                return "Contact was not added"
            elif command == "yes":
                break

    contacts[name] = phone

    return f"Contact {operation_type}."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        
        return "Contact updated."
    else:
        return "Contact was not found."


@input_error
def show_contact(args: list, contacts: dict) -> str:
    name = args.pop()

    return f"{name} has phone: {contacts[name]}"


@input_error
def show_all_contacts(contacts: dict) -> str:
    data = "\n".join([f"{name} has phone: {phone}" for name, phone in contacts.items()])

    return data
