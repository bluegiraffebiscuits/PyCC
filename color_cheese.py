cheese = {"cheese1": "swiss",
          "cheese2": "cheddar",
          "cheese3": "american",
          "cheese4": "parmesan"
          }

for number, variation in cheese.items():
    print(number.title() + " is " + variation.title() + ".")

