from app import App
from board import Board
import cursor

# ANSI Escape Sequences Reference: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def main():
    # Create each player's board.
    player1 = Board("Player 1")
    player2 = Board("Player 2")
    players = [player1, player2]
    
    # Create the Battleship app.
    app = App(player1, player2)

    # Prompt the user to enter the number of ships to be played.
    app.prompt_num_ships()

    # Give each player a chance to place their ships.
    for player in players:
        cursor.erase()
        action = input(f"\n{player.name}, press Enter to begin placing your ships...")
        app.check_quit(action)

        cursor.move_up(1)
        cursor.erase()

        print(player.name + "'s turn to place their ships")

        # For each ship in the player's arsenal.
        for ship in range(app.num_ships):
            cursor.erase()
            app.print_board(player)

            print("Coordinate input format: A1")
            print("Valid x-coordinates: A - J")
            print("Valid y-coordinates: 1 - 10")

            while True:
                # If the ship size is 1, assign both bow and stern to the same coordinate.
                if ship == 0:
                    stern = bow = app.prompt_ship_coordinate(ship, "rear")
                else:
                    stern = app.prompt_ship_coordinate(ship, "rear") # Rear coordinate of the ship.
                    bow = app.prompt_ship_coordinate(ship, "front") # Front coordinate of the ship.

                # Place the player's ship on their board.
                if app.place_ship(player, stern, bow, ship + 1):
                    break

            # Move the cursor to the line after "Player #'s turn to place their ships".
            cursor.move_to(4)

        cursor.erase()
        app.print_board(player) # Ensure board prints on last turn.

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"{player.name}, press Enter after reviewing your ship placements...")
        app.check_quit(action)

        # Move the cursor to the line after "Enter the number of ships" to
        # prepare to clear the screen for Player 2 to place their ships.
        cursor.move_to(2)

    # Begin the game loop.
    current_player = 0
    while True:
        cursor.move_to(0)
        cursor.erase()

        print(players[current_player].name + "'s turn to attack\n")
        action = input(f"{players[current_player].name}, press Enter to begin attacking...")
        app.check_quit(action)

        cursor.move_up(1)
        cursor.erase()

        print("Your Board")
        app.print_board(players[current_player])
        print("Enemy's Board")
        app.print_board(players[current_player], censored = True)

        coord = app.prompt_attack_coordinate()
        hit, sink = app.attack(players[abs(current_player - 1)], coord)

        if hit or sink:
            status = "Hit" if hit else "Sunk"
            print(f"\n{status} {players[abs(current_player - 1)]}'s ship!")
            continue

        print("\nMissed...")

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"\n{players[current_player].name}, press Enter when you're done reviewing you attacks...")
        app.check_quit(action)

        current_player = abs(current_player - 1)

        # NOTE: Generic prints for now. I just want to debug attack. Currently using player1 and player2 instead of a variable that grabs current player.
        # this isnt a game loop yet its just for debug purposes.

        # print("Player 1's turn")
        # print("Your Board")
        # app.print_board(player1)
        # print("Enemies Board")
        # app.print_board(player2, censored=True)

        # pos = app.prompt_attack_coordinate()
        # hit, sink = app.attack(player2, pos)

        # if not hit:
        #     print("MISSED!")
        # if hit:
        #     print(f"HIT PLAYER 2 @ {pos}")
        # if sink:
        #     print("SUNK PLAYERS SHIP OF SIZE X")

        # print("Player 2's turn")
        # print("Your Board")
        # app.print_board(player2)
        # print("Enemies Board")
        # app.print_board(player1, censored=True)

        # break


if __name__ == "__main__":
    main()
