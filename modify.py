spooka = {"color": "white", "type": "stealthy", "Health": 400,
           "Health_Bar": "green"}
print("Spookas' max health is " + str(spooka["Health"]))

if spooka["Health"] >= 350:
    print("High health.")
elif spooka["Health"] <= 350:
    print("Low health.")
else:
    print("Dead.")
