Cheese = ["swiss", "cheddar", "parmesan"]

print("\nHere is the append method:")
Cheese.append("brie")
print(Cheese)

print("\nHere is the insert method:")
Cheese.insert(2, "american")
print(Cheese)

print("\nHere is the del statement:")
del Cheese[0]
print(Cheese)

print("\nHere is the pop method:")
I_ate =  Cheese.pop(0)
print("I ate " + I_ate.title() + " Cheese.")




