def entitys(health, *enemies):
    """Summarize the enemies we are about to make."""
    print("\nAdding a " + str(health) +
          "-health enemy:")
    for enemy in enemies:
        print("- " + enemy)

entitys(400, "spoof")
entitys(250, "crystalite", "stone_knight")
