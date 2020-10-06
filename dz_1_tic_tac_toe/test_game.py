"""tests"""
import itertools
import unittest
from dz_1_tic_tac_toe import game


class GameTestCase(unittest.TestCase):
    """game tests"""

    def setUp(self):
        self.game = game.TicTacToe()

    def check_other_empty(self, state, not_empty):
        """check_other_empty"""
        for i, line in enumerate(state):
            for j, elem in enumerate(line):
                if [i, j] not in not_empty:
                    self.assertEqual(elem, "_")

    def test_toggle_player(self):
        """toggle_player func test"""

        self.assertEqual(self.game.curr_player, "X")
        self.game.toggle_players()
        self.assertEqual(self.game.curr_player, "O")
        self.game.toggle_players()
        self.assertEqual(self.game.curr_player, "X")

    def test_player_move(self):
        """apply_move func test"""
        ok_moves = list(itertools.permutations([0, 1, 2], 2))
        moves = []
        for move in ok_moves:
            moves.append(move)
            self.game.apply_move(list(move))
            self.assertEqual(self.game.state[move[0]][move[1]], "X")

    def test_validate_move(self):
        """ validate_move func test """
        try:
            self.game.validate_input("qwe 2 4")
        except game.InvalidInputError as ex:
            self.assertEqual(self.game.inv_args_count, str(ex))

        try:
            self.game.validate_input("22 3")
        except game.InvalidInputError as ex:
            self.assertEqual(self.game.inv_number, str(ex))

        try:
            self.game.validate_input("qwe ghj")
        except game.InvalidInputError as ex:
            self.assertEqual(self.game.inv_value, str(ex))

        try:
            self.game.apply_move([1, 1])
            self.game.validate_input("1 1")
        except game.InvalidInputError as ex:
            self.assertEqual(self.game.inv_state, str(ex))

        self.assertEqual(self.game.validate_input("   0 1  "), [0, 1])
        self.assertEqual(self.game.validate_input("2 1"), [2, 1])


if __name__ == "__main__":
    unittest.main()
