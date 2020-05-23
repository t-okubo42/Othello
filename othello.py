white = 0
black = 1
board_size = 8

class ReversiBoard(object):
    def __init__(self):
        self.cells = []
        for i in range(board_size):
            self.cells.append([None for i in range(board_size)])

        self.cells[3][3] = white
        self.cells[3][4] = black
        self.cells[4][3] = black
        self.cells[4][4] = white

class ReversiBoard(object):
    def put_disk(self, x, y, player):

        if self.cells[y][x] is not None:
            return False

        flippable = self.list_flippable_disks(x, y, player)
        if flippable == []:
            return False

        self.cells[y][x] = player
        for x,y in flippable:
            self.cells[y][x] = player

        return True