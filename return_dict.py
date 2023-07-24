def me(first_name, last_name, age="", favorite_cheese=""):
    """Make a dictionary about Liam"""
    Myself = {"first": first_name, "last": last_name}
    age = False
    favorite_cheese = True
    if age:
        Myself["age"] = age
    if favorite_cheese:
        Myself["favorite_cheese"] = favorite_cheese
    return Myself

programmer = me("Liam", "McConkey", age=11, favorite_cheese="parmesan")
print(programmer)

