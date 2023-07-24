ghosts = []

for spoof_number in range(6):
    spoof = {"color": "white", "health": "350", "speed": "medium"}
    ghosts.append(spoof)

for ghost in ghosts[:3]:
    print(ghost)
print("\nthey're more...")

print("\nTotal number of spoofs: " + str(len(ghosts))) 
