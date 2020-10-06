"""main script"""
from dz_1_tic_tac_toe import game

if __name__ == "__main__":

    while True:
        tic_tac_toe = game.TicTacToe()
        tic_tac_toe.start()
        print("\n\n\nanother one? Yes?: ", end="")
        if input() != "Yes":
            break
    print("bye!")
