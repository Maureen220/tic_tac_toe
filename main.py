import random
from art import art

BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
IS_PLAYING = True


def board_init(board_list):
    print("")
    print(f" {board_list[0]}  | {board_list[1]}  | {board_list[2]} ")
    print("-----------")
    print(f" {board_list[3]}  | {board_list[4]}  | {board_list[5]} ")
    print("-----------")
    print(f" {board_list[6]}  | {board_list[7]}  | {board_list[8]} ")
    print("")


def reset_board():
    global BOARD
    global IS_PLAYING
    BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    IS_PLAYING = True


def check_winner(board_list):
    global IS_PLAYING
    # Check rows
    for i in range(0, 9, 3):
        if board_list[i] == board_list[i + 1] == board_list[i + 2]:
            IS_PLAYING = False
            return True

    # Check columns
    for i in range(3):
        if board_list[i] == board_list[i + 3] == board_list[i + 6]:
            IS_PLAYING = False
            return True

    # Check diagonals
    if board_list[0] == board_list[4] == board_list[8] or board_list[2] == board_list[4] == board_list[6]:
        IS_PLAYING = False
        return True

    return False


def user_first_player(board_list):
    # User's turn
    usr_turn_01 = int(input("Which tile would you like to update? ")) - 1
    board_list[usr_turn_01] = "X"
    board_init(board_list)

    if check_winner(board_list):
        print("User Wins! ╰(*°▽°*)╯")
        return False  # Game is over

    return True  # Continue the game


def comp_first_player(board_list):
    # Computer's turn
    numbers_to_choose_from = [num for num in board_list if num != "X" and num != "O"]
    print("Computer's turn: ")
    comp_turn_01 = int(random.choice(numbers_to_choose_from)) - 1
    board_list[comp_turn_01] = "O"
    board_init(board_list)

    if check_winner(board_list):
        print("Comp Wins! (╯°□°）╯︵ ┻━┻")
        return False  # Game is over

    return True  # Continue the game


def play_game():
    print(art)

    first_player = random.choice([True, False])
    first_loop = True

    while IS_PLAYING:
        if first_player:
            if first_loop:
                print("You were randomly selected to go first.")
                board_init(BOARD)
                first_loop = False
            if not user_first_player(BOARD):
                break
        else:
            if first_loop:
                print("Computer was randomly selected to go first.")
                first_loop = False
            if not comp_first_player(BOARD):
                break

        # Switch turns
        first_player = not first_player
    reset_board()


while input("Do you want to play a game of Tic Tac Toe? Type 'y' and 'n': ").lower() == "y":
    play_game()
