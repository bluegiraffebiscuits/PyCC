def entitys(*enemies):
    """Summarize the enemies we are about to make."""
    print("\nAdding an enemy:")
    for enemy in enemies:
        print("- " + enemy.title())

entitys("spoof")
entitys("crystalite", "stone_knight")