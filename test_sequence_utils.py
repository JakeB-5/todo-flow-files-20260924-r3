import unittest

from sequence_utils import ordered_unique


class OrderedUniqueTests(unittest.TestCase):
    def test_repeated_values_keep_first_occurrence_order(self):
        values = [3, 1, 3, 2, 1, 4, 2]
        self.assertEqual(ordered_unique(values), [3, 1, 2, 4])

    def test_hashable_strings_and_tuples(self):
        values = ["b", (1, 2), "a", "b", (1, 2)]
        self.assertEqual(ordered_unique(values), ["b", (1, 2), "a"])

    def test_empty_input(self):
        values = []
        result = ordered_unique(values)
        self.assertEqual(result, [])
        self.assertEqual(values, [])
        self.assertIsNot(result, values)

    def test_already_unique_input(self):
        values = [5, 2, 9]
        result = ordered_unique(values)
        self.assertEqual(result, [5, 2, 9])
        self.assertEqual(values, [5, 2, 9])
        self.assertIsNot(result, values)

    def test_repeated_input_is_unchanged(self):
        values = ["c", "a", "c", "b", "a"]
        original = values.copy()
        result = ordered_unique(values)
        self.assertEqual(values, original)
        self.assertEqual(result, ["c", "a", "b"])
        self.assertIsNot(result, values)

    def test_iterator_input(self):
        self.assertEqual(ordered_unique(iter([2, 1, 2, 3])), [2, 1, 3])


if __name__ == "__main__":
    unittest.main()
