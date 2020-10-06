"""tic tac toe game"""
import typing as tp


class InvalidInputError(Exception):
    """input exception"""


class GameError(Exception):
    """invalid game state"""


class TicTacToe:
    """game class"""

    inv_args_count = "invalid move, args count != 2, try again"
    inv_value = "invalid move, not int, try again"
    inv_number = "invalid move, out of field, try again"
    inv_state = "invalid move, this cell is occupied, try again"

    def __init__(self):
        self._empty = "_"
        self.state = [[self._empty for i in range(3)] for j in range(3)]
        self.curr_player = "X"
        self.winner = None

    def __str__(self):
        return "\n".join("\t".join("%s" % x for x in y) for y in self.state)

    def find_winner_in_line(self) -> bool:
        """find_winner_in_line"""
        for line in self.state:
            if line.count(line[0]) == len(line) and line[0] != "_":
                self.winner = line[0]
                return True
        return False

    def find_winner_in_row(self) -> bool:
        """find_winner_in_row"""
        for i in range(3):
            if (
                self.state[0][i]
                == self.state[1][i]
                == self.state[2][i]
                != self._empty
            ):
                self.winner = self.state[0][i]
                return True
        return False

    def find_winner_in_cross(self):
        """find_winner_in_cross"""
        if (
            self.state[0][0]
            == self.state[1][1]
            == self.state[2][2]
            != self._empty
        ):
            self.winner = self.state[1][1]
            return
        if (
            self.state[0][2]
            == self.state[1][1]
            == self.state[2][0]
            != self._empty
        ):
            self.winner = self.state[1][1]

    def check_winner(self) -> None:
        """check_winner"""
        if self.find_winner_in_line():
            return
        if self.find_winner_in_row():
            return
        self.find_winner_in_cross()

    def validate_input(self, inp: str) -> tp.List[int]:
        """user input validation"""
        move_str = inp.strip().split(" ")
        if len(move_str) != 2:
            raise InvalidInputError(self.inv_args_count)
        try:
            move = [int(x) for x in move_str]
        except ValueError as ex:
            raise InvalidInputError(self.inv_value) from ex

        if any(x > 2 or x < 0 for x in move):
            raise InvalidInputError(self.inv_number)

        if self.state[move[0]][move[1]] != self._empty:
            raise InvalidInputError(self.inv_state)

        return move

    def get_current_player_move(self) -> tp.List[int]:
        """get move from console"""
        while True:
            print(f"{self.curr_player} move: ", end="")
            try:
                return self.validate_input(input())
            except InvalidInputError as ex:
                print(ex)

    def toggle_players(self) -> None:
        """change current player"""
        if self.curr_player == "X":
            self.curr_player = "O"
        elif self.curr_player == "O":
            self.curr_player = "X"
        else:
            raise GameError(
                f"invalid state current player is {self.curr_player}"
            )

    def apply_move(self, move: tp.List[int]) -> None:
        """apply move"""
        try:
            self.state[move[0]][move[1]] = self.curr_player
        except IndexError as ex:
            raise GameError(f"invalid move {move}") from ex

    def start(self) -> None:
        """start of whole game"""
        while not self.winner:
            print(self)
            move = self.get_current_player_move()
            self.apply_move(move)
            self.check_winner()
            self.toggle_players()
        print(f"winner is {self.winner}")


if __name__ == "__main__":

    while True:
        tic_tac_toe = TicTacToe()
        tic_tac_toe.start()
        print("\n\n\nanother one? Yes?: ", end="")
        if input() != "Yes":
            break
    print("bye!")
