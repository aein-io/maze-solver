import time
from cell import Cell
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)

    def _create_cells(self):
        for _ in range(self._num_cols):
            col = []
            for _ in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while True:
            to_visit = []

            for x, y in directions:
                curr_x, curr_y = i + x, j + y
                if 0 <= curr_x < len(self._cells) and 0 <= curr_y < len(self._cells[0]):
                    if not self._cells[curr_x][curr_y].visited:
                        to_visit.append((curr_x, curr_y))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_cell = random.choice(to_visit)

            if next_cell[0] == i - 1:  # If the neighbor is on top
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            elif next_cell[0] == i + 1:  # If the neighbor is below
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            elif next_cell[1] == j - 1:  # If this neighbor is to the left
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            elif next_cell[1] == j + 1:  # If the neighbor is to the right
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False

            self._break_walls(next_cell[0], next_cell[1])
