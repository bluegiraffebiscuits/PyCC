prompt = "Give us your name, so we repeat it back"
prompt += "\nYou can type 'stop program' to quit."
prompt += "\nSooo, What's your first name? "

running = True
while running:
    message = input(prompt)

    if message == "stop program":
        running = False
    else:
        print(message)


