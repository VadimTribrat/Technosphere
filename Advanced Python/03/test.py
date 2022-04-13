import unittest
from customlist import CustomList


class TestClass(unittest.TestCase):
    def test_sub_add(self):
        cl1 = CustomList([5, 1, 3, 7])
        cl2 = CustomList([1, 2, 7])
        self.assertEqual(cl1 - cl2, CustomList([4, -1, -4, 7]))
        self.assertEqual(cl1, CustomList([5, 1, 3, 7]))
        self.assertEqual(cl2, CustomList([1, 2, 7]))
        self.assertEqual(cl1 + cl2, CustomList([6, 3, 10, 7]))
        self.assertEqual(cl1, CustomList([5, 1, 3, 7]))
        self.assertEqual(cl2, CustomList([1, 2, 7]))
        self.assertEqual(cl1 - [1, 2, 7], CustomList([4, -1, -4, 7]))
        self.assertEqual(cl1, CustomList([5, 1, 3, 7]))
        self.assertEqual(cl1 + [1, 2, 7], CustomList([6, 3, 10, 7]))
        self.assertEqual(cl1, CustomList([5, 1, 3, 7]))
        self.assertEqual([1, 2, 7] + cl1, CustomList([6, 3, 10, 7]))
        self.assertEqual([5, 1, 3, 7] + -cl2, CustomList([4, -1, -4, 7]))

    def test_eq_lt(self):
        cl1 = CustomList([5, 1, 3, 7])
        self.assertEqual(cl1.__repr__(), '[5, 1, 3, 7]')
        self.assertTrue(CustomList([5, 1, 3, 7]) == CustomList([16]))
        self.assertTrue(CustomList([5, 1, 3, 7]) < CustomList([17]))
        self.assertTrue(CustomList([5, 1, 3, 7]) >= CustomList([16]))
        self.assertTrue(CustomList([5, 1, 3, 7]) <= CustomList([16]))
        self.assertTrue(CustomList([5, 1, 3, 7]) > CustomList([15]))
        self.assertTrue(CustomList([5, 1, 3, 7]) != CustomList([1]))


if __name__ == "__main__":
    unittest.main()
