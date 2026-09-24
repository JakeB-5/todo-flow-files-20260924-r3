import unittest

from text_utils import compact


class CompactTests(unittest.TestCase):
    def test_mixed_whitespace(self):
        self.assertEqual(compact(" \talpha  \t beta\n\ngamma\r\n delta \t\n"), "alpha beta gamma delta")

    def test_empty_and_whitespace_only(self):
        for text in ("", " ", "\t\n\r\v\f", " \t \n ", "\u00a0\u2003\u2028"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), "")

    def test_unicode_whitespace(self):
        self.assertEqual(compact("\u2003alpha\u00a0\u2009beta\u2028gamma\u3000"), "alpha beta gamma")

    def test_already_compact_text(self):
        for text in ("alpha", "alpha beta gamma", "Hello, world!", "café 東京"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), text)


if __name__ == "__main__":
    unittest.main()
