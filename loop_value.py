favorite_cheeses = {"John": "american",
            "Fred": "cheddar",
            "Raj": "american",
            "Greg": "parmesan"}

print("These cheeses are some favorites among people:")
for cheese in set(favorite_cheeses.values()):
    print(cheese.title()) 
