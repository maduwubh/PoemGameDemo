def print_title():
    print("=" *50)
    print("       Welcome to the Poem Game")
    print("=" *50)

def print_registered_players(players):
    print("\nRegistered Players:\n")
    
    for index, player in enumerate(players, start=1):
        print(f"{index}. {player.name}")