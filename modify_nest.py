ghosts = []

for ghost in range(0,6):
    spoof = {"color": "white", "health": 350, "speed": "medium"}
    ghosts.append(spoof)

for ghost in ghosts[0:2]:
    if ghost["speed"] == "medium":
        ghost["color"] = "blue"
        ghost["health"] = 400
        ghost["speed"] = "fast"
    elif ghost["speed"] == "fast":
        ghost["color"] = "orange"
        ghost["health"] = 200
        ghost["speed"] = "slow"

for ghost in ghosts[0:5]:
    print(ghost)
print("There are more...")
    

