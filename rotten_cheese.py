rotten_cheeses = ["swiss", "american", "cheddar"]
fresh_cheeses = []

while rotten_cheeses:
    current_cheese = rotten_cheeses.pop()
    
    print("We're making a new batch of " + current_cheese.title())
    fresh_cheeses.append(current_cheese)

print("\nWe have made new batches of:")
for fresh_cheese in fresh_cheeses:
    print(fresh_cheese.title())
