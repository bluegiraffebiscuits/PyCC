def cheese_sentence(first_cheese, second_cheese): 
    """Display what your 2 favorite cheeses are."""
    print("\nA cheese I like is " + first_cheese.title() + " cheese.")
    print("Another cheese I like is " + second_cheese.title() + " cheese.")

cheese_sentence("american", "parmesan")   
cheese_sentence(first_cheese="american", second_cheese="parmesan")