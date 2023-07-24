rotten_cheeses = ["parmesan", "cheddar", "american"]
fresh_cheeses = []

while rotten_cheeses:
    current_cheeses = rotten_cheeses.pop()
    print("Making a new batch of fresh " + (current_cheeses.title()) + " cheese.")
    fresh_cheeses.append(current_cheeses)

print("\nWe have make new fresh batches of:")
for fresh_cheese in fresh_cheeses:
    print(" " + fresh_cheese.title() + " cheese")