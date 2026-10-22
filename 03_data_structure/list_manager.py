# List of Players
players = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Salah"]

# Accessing elements
print(f"First Player: {players[0]}") # Messi
print(f"Last Player: {players[-1]}") # Salah

# Modifying the list
players.append("Lewandowski") # Add player
players.remove("Neymar")       # Remove player
players[1] = "Kante"           # Update player

print(f"Updated Squad: {players}")

# Iterating through the list with a break condition
for player in players:
    print(f"Checking: {player}")
    if player == "Mbappe":
        print("Target Player Found!")
        break
else:
    print("Player Not Found")
