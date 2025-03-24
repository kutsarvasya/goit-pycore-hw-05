def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "User not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if finding_user_in_obj(name, contacts):
        return 'User already exists'
    contacts[name] = phone
    return "Contact added."


@input_error
def finding_user_in_obj(name, obj):
    for k in obj:
        if name.lower() == k.lower():
            return True
    return False


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if not finding_user_in_obj(name, contacts):
        raise KeyError
    contacts[name] = phone
    return 'Updated'


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if finding_user_in_obj(name, contacts):
        return contacts[name]
    raise KeyError
