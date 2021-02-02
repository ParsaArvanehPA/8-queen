import random


class SaSolver:
    def __init__(self):
        self.queen_num = 8
        self.chess_board = []
        self.current_board = []
        self.temp = 20000
        self.solved = False

    def chess_board_filler(self):
        for counter in range(self.queen_num):
            self.chess_board.append(random.randint(0, 7))
        self.current_board = self.chess_board

    def printer(self):
        for index in range(self.queen_num):
            print(f"({index}, {self.chess_board[index]})")

    def sa(self):
        while self.temp > 0:
            next_board = []

            for index in range(self.queen_num):
                next_board.append(index)

            random_row = random.randint(0, 7)
            random_column = random.randint(0, 7)

            for index in range(self.queen_num):
                if index == random_column:
                    next_board[index] = random_row
                else:
                    next_board[index] = self.current_board[index]

            delta = self.costCalculator(
                self.current_board) - self.costCalculator(next_board)
            probability = 2.7 ** (delta/self.temp)
            print("====>", probability)
            if delta > 0:
                # self.chess_board = next_board
                self.current_board = next_board
                self.temp -= 1
            else:
                move_probability = random.randint(0, 1000000)
                if move_probability <= probability:
                    # self.chess_board = next_board
                    self.current_board = next_board
                self.temp -= 1

            if self.costCalculator(self.current_board) == 0:
                self.solved = True
                break

        if self.solved:
            self.chess_board = self.current_board
            print('solution found')
            self.printer()
        else:
            print(self.temp)
            print('solution not found')

    def costCalculator(self, array):
        threat = 0
        for i in range(self.queen_num):
            for j in range(i+1, self.queen_num):
                if (array[i] == array[j]) or (abs(i - j) == abs(array[i] - array[j])):
                    threat += 1

        return threat


if __name__ == '__main__':
    SA = SaSolver()
    SA.chess_board_filler()
    SA.printer()
    SA.sa()
