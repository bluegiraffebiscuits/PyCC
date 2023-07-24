def love_cheese(variations):
    """Print you loving your favorite cheeses"""
    for variation in variations:
        msg = ("I love " + variation.title() + " cheese.")
        print(msg)

cheeses = ["american", "parmesan", "cheddar"]
love_cheese(cheeses)


