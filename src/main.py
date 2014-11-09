from game_manager import GameManager

def main():
    game_manager = GameManager()

    game_manager.initialize()

    while game_manager.running():
        game_manager.tick()

    game_manager.clean_up()

main()
