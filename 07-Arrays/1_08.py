computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
sorted_computer_games = sorted(computer_games)

game_number = 0
while game_number < len(computer_games):
    print(f"{game_number+1}. {computer_games[game_number]}")
    game_number += 1 