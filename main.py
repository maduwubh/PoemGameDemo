from services.game_service import GameService

from utils.display import print_title, print_registered_players

def main():
    print_title()
    
    game = GameService()
    game.register_player()
    game.display_players()
    
    
    
if __name__ == "__main__":
    main()