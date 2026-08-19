from models.player import Player
from utils.display import print_registered_players


class GameService:

    def __init__(self):
        self.players = []

    def register_player(self):

        while True:

            try:
                total_players = int(input("Enter number of players: "))

                if total_players < 2:
                    print("At least 2 players are required.\n")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.\n")

        print()

        for number in range(1, total_players + 1):

            while True:

                name = input(f"Enter Player {number} Name: ").strip()

                if name == "":
                    print("Player name cannot be empty.\n")
                    continue

                self.players.append(Player(name))
                break

    def display_players(self):
        print_registered_players(self.players)