feedback = {}

cheese_polling = True

while cheese_polling:
    name = input("\nWhat's your name? ")
    question = input("What's your favorite cheese? ")

    feedback[name] = question

    repeat = input("\nDo you want to share this poll with another person? (yes/nah) ")
    if repeat == "nah":
        cheese_polling = False

    print("\n---CHEESE POLL RESULTS ARE IN---")
    for name, question in feedback.items():
        print(name + "'s favorite type of cheese is " + question + ".")
