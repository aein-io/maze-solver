import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols,)
        self.assertEqual(len(m1._cells[0]), num_rows,)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[num_cols - 1]
                         [num_rows - 1].has_bottom_wall, False)

    def test_maze_reset_cells_visited(self):
        num_cols = 3
        num_rows = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(m._num_cols):
            for j in range(m._num_rows):
                self.assertEqual(m._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
