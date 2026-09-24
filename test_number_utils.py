import unittest

from number_utils import safe_divide


class SafeDivideTests(unittest.TestCase):
    def test_nonzero_division(self):
        for numerator, denominator, expected in [
            (7, 2, 3.5),
            (-7, 2, -3.5),
            (7, -2, -3.5),
            (-7, -2, 3.5),
            (0, 2, 0.0),
        ]:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(safe_divide(numerator, denominator), expected)

    def test_zero_denominator_defaults_to_none(self):
        for denominator in (0, 0.0, -0.0):
            with self.subTest(denominator=denominator):
                self.assertIsNone(safe_divide(7, denominator))

    def test_zero_denominator_returns_exact_fallback(self):
        fallback = object()
        self.assertIs(safe_divide(7, 0, fallback), fallback)
        self.assertEqual(safe_divide(0, 0, fallback="undefined"), "undefined")

    def test_nonzero_denominator_ignores_fallback(self):
        self.assertEqual(safe_divide(9, 2, fallback="unused"), 4.5)

    def test_invalid_operands_propagate_type_error(self):
        for numerator, denominator in [("7", 2), (7, "2"), (None, 2)]:
            with self.subTest(numerator=numerator, denominator=denominator):
                with self.assertRaises(TypeError):
                    safe_divide(numerator, denominator, fallback="unused")

    def test_custom_division_error_is_not_suppressed(self):
        class FailingNumerator:
            def __truediv__(self, denominator):
                raise ValueError("division failed")

        with self.assertRaisesRegex(ValueError, "division failed"):
            safe_divide(FailingNumerator(), 2, fallback="unused")


if __name__ == "__main__":
    unittest.main()
