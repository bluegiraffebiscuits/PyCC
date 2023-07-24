def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()
random_kid = get_formatted_name("Liam", "Elliot", "McConkey")
print(random_kid)