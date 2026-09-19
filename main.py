import messages
import game_logic

def main():
    messages.welcome_message()
    play = True
    while play:
        game_logic.game()
        play = messages.play_again()

if __name__ == "__main__":
    main()
