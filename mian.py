from assets.story import *

#core game
#structure from start to end    
def main():
    while True:
        start_menu()
        base_game()
        ending_sec()
        # If restart() returns False, break the loop and end the game
        if not restart():
            break

if __name__ == '__main__':
    main()