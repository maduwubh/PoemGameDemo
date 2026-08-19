from models.player import Player
from utils.display import print_registered_players
from models.poem import Poem
from services.random_selector import RandomSelector


class GameService:

    def __init__(self):
        self.players = []
        self.poem = None
        self.current_player = None
        self.started = False

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
    
    def add_players(self, names):
        self.players = [Player(name) for name in names if name.strip()]

    def start_game(self, title="Untitled Poem"):
        self.poem = Poem(title)
        self.started = True
        self.current_player = self._pick_next_player()
        return self.current_player

    def _pick_next_player(self):
        remaining = [p for p in self.players if not p.has_played]
        if not remaining:
            return None
        return RandomSelector.select_random_item(remaining)

    def submit_line(self, text):
        if self.current_player is None or not text.strip():
            return
        self.poem.add_line(self.current_player.name, text.strip())
        self.current_player.mark_as_played()
        self.current_player = self._pick_next_player()

    def is_over(self):
        return self.started and self.current_player is None