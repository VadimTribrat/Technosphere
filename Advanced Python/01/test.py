import unittest
from tictactoe import TicTacToe


class TestClass(unittest.TestCase):
    def setUp(self):
        self.tic_tac = TicTacToe()

    def test_winx_1(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 0)
        ans[0] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 0)
        ans[6] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 2)
        ans[8] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_2(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(2, 0)
        ans[6] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_3(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 0)
        ans[0] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_4(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(1, 0)
        ans[3] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 2)
        ans[5] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_5(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(2, 0)
        ans[6] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 2)
        ans[8] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_6(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 0)
        ans[0] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 0)
        ans[3] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 2)
        ans[8] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 0)
        ans[6] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_7(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 1)
        ans[1] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 0)
        ans[0] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_winx_8(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 2)
        ans[2] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 2)
        ans[5] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 0)
        ans[6] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 2)
        ans[8] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_wino_1(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 0)
        ans[0] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 0)
        ans[3] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_draw(self):
        ans = ['.' for _ in range(9)]
        self.tic_tac.move(0, 0)
        ans[0] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 1)
        ans[1] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 0)
        ans[3] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 1)
        ans[4] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 1)
        ans[7] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 0)
        ans[6] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(0, 2)
        ans[2] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(2, 2)
        ans[8] = 'o'
        self.assertEqual(self.tic_tac.board, ans)
        self.tic_tac.move(1, 2)
        ans[5] = 'x'
        self.assertEqual(self.tic_tac.board, ans)
        self.assertEqual(self.tic_tac.is_over, True)
        self.tic_tac.show_board()

    def test_correct_input(self):
        self.assertRaises(Exception, self.tic_tac.move, 0, 3)
        self.assertRaises(Exception, self.tic_tac.move, 3, 0)
        self.assertRaises(Exception, self.tic_tac.move, -1, 2)
        self.assertRaises(Exception, self.tic_tac.move, 2)
        self.assertRaises(Exception, self.tic_tac.move, -2)
        self.assertRaises(Exception, self.tic_tac.move, 1)
        self.assertRaises(Exception, self.tic_tac.move, "abra c", [1, 2, 3])
        self.assertRaises(Exception, self.tic_tac.move, 2, "abra")
        self.assertRaises(Exception, self.tic_tac.move, set(), 1)

    def test_occupied_positions(self):
        self.tic_tac.move(1, 1)
        self.assertRaises(Exception, self.tic_tac.move, 1, 1)
        self.tic_tac.move(0, 0)
        self.assertRaises(Exception, self.tic_tac.move, 0, 0)
        self.tic_tac.move(0, 1)
        self.assertRaises(Exception, self.tic_tac.move, 0, 1)


if __name__ == "__main__":
    unittest.main()
