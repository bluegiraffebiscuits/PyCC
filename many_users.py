users = {
    "jhapsburg": {
        "first": "Juan",
        "last": "Hapsburg",
        "location": "Detroit"
    },

    "phapsburg": {
        "first": "Pedro",
        "last": "Hapsburg",
        "location": "Chicago"
    },

}

for online_name, person_info in users.items():
    print("\nUsername: " + online_name)
    full_name = person_info["first"] + " " + person_info["last"]
    location = person_info["location"]

    print("\tFull name: " + full_name)
    print("\tLocation: " + location)