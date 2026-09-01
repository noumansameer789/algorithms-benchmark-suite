import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from algorithms.core import equal_range, insertion_sort, merge_sort


class AlgorithmsTest(unittest.TestCase):
    def test_sorts_and_instruments(self):
        source = [5, 1, 3, 3, -2]
        for algorithm in (insertion_sort, merge_sort):
            result = algorithm(source)
            self.assertEqual(result.values, sorted(source))
            self.assertGreater(result.steps, 0)

    def test_equal_range(self):
        self.assertEqual(equal_range([1, 2, 2, 2, 4], 2), (1, 4))
        self.assertEqual(equal_range([1, 2, 4], 3), (2, 2))


if __name__ == "__main__":
    unittest.main()
