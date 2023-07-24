favorite_cheeses = {"John": "american",
                    "Fred": "cheddar",
                    "Raj": "swiss",
                    "Greg": "parmesan",
                    "Thomas": "brie"}

cool_people = ["Raj", "Fred"]
for people in favorite_cheeses.keys():
    print(people)

    if people in cool_people:
        print(" Hey " + people + ", you have a good opinion because " +
              favorite_cheeses[people].title() + " is a good cheese")
if "brie" not in favorite_cheeses:
    print(" i hate you")

