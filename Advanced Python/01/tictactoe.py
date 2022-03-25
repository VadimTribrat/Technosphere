class TicTacToe:
    def __init__(self):
        self.__board = ['.' for _ in range(9)]
        self.__num_of_x = 0
        self.__num_of_o = 0
        self.__is_over = False

    @property
    def is_over(self):
        return self.__is_over

    @property
    def board(self):
        return self.__board

    def show_board(self):
        for i in range(2, -1, -1):
            for j in range(3):
                print(self.__board[i*3 + j], end=' ')
            print()
        print()

    def move(self, row_num=-1, col_num=-1):
        if self.__is_over:
            print("Gave over")
            return
        i, j = 0, 0
        if row_num == -1 and col_num == -1:
            i, j = self.get_index()
        else:
            i, j = row_num, col_num
            cond = 0 <= i < 3 and 0 <= j < 3 and self.__board[i*3+j] == '.'
            if not cond:
                raise IndexError(
                    "Must be two integers from"
                    "0 to 2 and field must be not occupied"
                )
        if self.__num_of_x < self.__num_of_o:
            self.__board[3*i + j] = 'x'
            self.__num_of_x += 1
        elif self.__num_of_x > self.__num_of_o:
            self.__board[3*i + j] = 'o'
            self.__num_of_o += 1
        else:
            self.__board[3*i + j] = 'x'
            self.__num_of_x += 1
        self.__is_over = self.validate()
        if self.__is_over:
            print('Game over')

    def validate(self):
        for i in range(3):
            condx_col = self.__board[i::3] == ['x']*3
            condx_row = self.__board[i*3:(i+1)*3] == ['x']*3
            condo_col = self.__board[i::3] == ['o']*3
            condo_row = self.__board[i*3:(i+1)*3] == ['o']*3
            if condx_col or condx_row:
                print('X win')
                return True
            if condo_col or condo_row:
                print('O win')
                return True
        if self.__board[0] == self.__board[4] == self.__board[8]:
            if self.__board[0] == 'x':
                print('X win')
            if self.__board[0] == 'o':
                print('O win')
            if self.__board[0] == 'x' or self.__board[0] == 'o':
                return True
        if self.__board[6] == self.__board[4] == self.__board[2]:
            if self.__board[6] == 'x':
                print('X win')
            if self.__board[6] == 'o':
                print('O win')
            if self.__board[6] == 'x' or self.__board[6] == 'o':
                return True
        if self.__num_of_o + self.__num_of_x == 9:
            print('Draw')
            return True
        return False

    def get_index(self):
        input_ = input()
        if len(input_.split()) != 2:
            raise IndexError("Must be two indexes separated by a space")
        try:
            i, j = list(map(int, input_.split()))
        except Exception:
            print("Must be two integers separated by a space")
            raise
        if not (0 <= i < 3 and 0 <= j < 3 and self.__board[i*3+j] == '.'):
            raise IndexError(
                "Must be two integers from "
                "0 to 2 and field must be not occupied"
            )
        return i, j

    def start_game(self):
        print("Input format: two non-negative integers from 0 to 2 ")
        print("(separated by a space) row and column numbers, respectevely.")
        while not self.__is_over:
            try:
                self.move()
            except IndexError as index_err:
                print(index_err)
            except Exception as exc:
                print(exc)
            else:
                self.show_board()


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.start_game()
