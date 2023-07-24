def get_full_name(first_name, last_name):
    """Return the full name"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nWhat's your name? ")
    print("Type 'stop program' to quit")
    name_1 = input("first name: ")
    if name_1 == "stop program":
        break
    name_2 = input("last name: ")
    if name_2 == "stop program":
        break
    full_person_name = get_full_name(name_1, name_2)
    print("\nHello there, " + full_person_name + ".")