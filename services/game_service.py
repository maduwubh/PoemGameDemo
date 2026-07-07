from models.player import Player
from utils.display import print_title, print_registeed_players

class GameService:
    def __init__(self):
        self.players = []
        
    def register_player(self):
        while True:
            try:
                total_players = int(input("Enter the number of players: "))
                
                if total_players < 2 or total_players > 4:
                    print("Atleast two players are required to play the game. Please enter a valid number of players.")
                    continue
            except ValueError:
                print("Please enter a valid number of players \n")
                
                print()
                
                for nu,ber in range(1, total_players + 1):
                    while True:
                        
                        name = input(f"Enter the name of player {number}: ").strip()
                        
                        if name == "":
                            print("Player name cannot be empty. Please enter a valid name.")
                            continue
                        
                    self.players.append(Player(name))