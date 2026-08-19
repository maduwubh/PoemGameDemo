from services.game_service import GameService
from utils.display import print_title


def main():
    print_title()

    game = GameService()
    game.register_player()
    game.display_players()

    title = input("\nEnter the title of the poem: ").strip() or "Untitled Poem"
    current = game.start_game(title)

    while not game.is_over():
        line = input(f"\n{current.name}, write your line: ")
        game.submit_line(line)
        current = game.current_player

    game.poem.display()


if __name__ == "__main__":
    main()