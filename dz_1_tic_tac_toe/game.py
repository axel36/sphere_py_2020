"""tic tac toe game"""
import typing as tp


class InvalidInputError(Exception):
    """input exception"""


class TicTacToe:
    """game class"""

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
            raise InvalidInputError("invalid move, too much args, try again")
        try:
            move = [int(x) for x in move_str]
        except ValueError as err:
            raise InvalidInputError(
                "invalid move, not int, try again"
            ) from err

        if self.state[move[0]][move[1]] != self._empty:
            raise InvalidInputError(
                "invalid move, this cell is occupied, try again"
            )
        if any(x > 2 or x < 0 for x in move):
            raise InvalidInputError("invalid move, out of field, try again")

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
            raise RuntimeError(
                f"invalid state current player is {self.curr_player}"
            )

    def apply_move(self, move: tp.List[int]) -> None:
        """apply move"""
        self.state[move[0]][move[1]] = self.curr_player

    def start(self) -> None:
        """start of whole game"""
        while not self.winner:
            print(self)
            move = self.get_current_player_move()
            self.apply_move(move)
            self.toggle_players()
            self.check_winner()
        print(f"winner is {self.winner}")
