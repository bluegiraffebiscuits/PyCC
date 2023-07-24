def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
random_kid = get_formatted_name("liam", "mcConkey")
print(random_kid)

random_kid = get_formatted_name("liam", "elliot", "mcConkey")
print(random_kid)