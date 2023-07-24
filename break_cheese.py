question = ("What's one of your favorite cheeses? ")
question += ("\nYou can type 'stop program' to quit the program ")

while True:
    response = input(question)

    if response == "stop program":
        break
    else:
        print("\n" + response.title() + " is a nice cheese.")