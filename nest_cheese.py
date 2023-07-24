cheese = {"texture": "holes",
           "tastes": ["sweet", "nutty"],}

print("If your cheese has " + cheese["texture"] + " in it...")

print("\nand it tastes:")
for taste in cheese["tastes"]:
    print(taste)

print("\nthen your cheese is swiss cheese!")