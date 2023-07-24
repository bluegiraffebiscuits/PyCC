def make_cheese(unmade_cheeses, fresh_cheeses):
    """
    Make cheese until no supplies are left.
    Move fresh cheese into fresh_cheeses
    """

    while unmade_cheeses:
        current_cheeses = unmade_cheeses.pop()
        #Say that you're making cheese.
        print("Making new cheese: " + current_cheeses)
        fresh_cheeses.append(current_cheeses)

def show_fresh_cheeses(fresh_cheeses):
    """Show the fresh cheese that has been made."""
    print("\nThe following cheese has been made:")
    for fresh_cheese in fresh_cheeses:
        print(fresh_cheese)

unmade_cheeses = ["parmesan", "american", "cheddar"]
fresh_cheeses = []

make_cheese(unmade_cheeses, fresh_cheeses)
show_fresh_cheeses(fresh_cheeses)

make_cheese(unmade_cheeses[:], fresh_cheeses)