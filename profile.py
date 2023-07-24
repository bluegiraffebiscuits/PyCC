def build_personal_info(first, last, **user_info):
    """Build a cool dictionary about Liam"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_personal_info("Liam", "McConkey",
                                   interests="Game Dev")

print(user_profile)
