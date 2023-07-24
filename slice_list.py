cheeses = ["swiss", "cheddar", "american", "parmesan"]
print(cheeses[1:3])

#You can just put the index of the last element to get the entire list.
cheeses = ["swiss", "cheddar", "american", "parmesan"]
print(cheeses[:4])

#You can just put the index of a specific element on the list, so the list only prints out that specific element and beyond
cheeses = ["swiss", "cheddar", "american", "parmesan"]
print(cheeses[1:])

cheeses = ["swiss", "cheddar", "american", "parmesan"]
print(cheeses[-2:])

cheeses = ["swiss", "cheddar", "american", "parmesan"]
print("These are my favorite types of cheese:")
for cheese in cheeses[:2]:
    print(cheese.title())