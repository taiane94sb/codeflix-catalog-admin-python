import unittest

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required_1(self):
        with self.assertRaises(TypeError):
            Category()

    def test_name_is_required_2(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_256_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a" * 256)


if __name__ == "__main__":
    unittest.main()
