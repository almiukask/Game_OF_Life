import unittest
from GameOfLife import get_neighbours_count


class TestStringMethods(unittest.TestCase):

    global grid
    grid = [
        [-1, -1, 1, 8, 1],
        [-1, 0, 1, 8, 8],
        [-1, 1, 1, 1, "b"],
        [0, 1, 0, 1, " "],
        [1, 1, 1, 1, 1],
    ]

    def test_01_numbers(self):
        self.assertEqual(get_neighbours_count(grid, 1, 1), 8)
        self.assertEqual(get_neighbours_count(grid, 3, 2), 8)
        self.assertEqual(get_neighbours_count(grid, 0, 4), 3)

    def test__02_not_a_number(self):
        with self.assertRaises(TypeError):
            get_neighbours_count(grid, 3, 3)

    def test_03_wrong_indexes(self):
        with self.assertRaises(Exception):
            get_neighbours_count(grid, -1, -1)
        with self.assertRaises(Exception):
            get_neighbours_count(grid, "a", "b")


if __name__ == "__main__":
    unittest.main()
