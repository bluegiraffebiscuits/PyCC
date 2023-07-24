cheeses = {"swiss": ["sweet", "nutty"],
           "american": ["salty"],
           "cheddar": ["sharp", "salty"],
           "parmesan": ["salty"]}

for variation, tastes in cheeses.items():
    print("\n " + variation.title() + " Cheese tastes:")
    for taste in tastes:
        print("\t" + taste.title())
