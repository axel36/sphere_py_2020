"""tests"""
import unittest
from dz_2_lru_i_slist import super_list


class SuperListTestCase(unittest.TestCase):
    """cache tests"""

    def setUp(self):
        self.slist1 = super_list.SuperList([1, 2, 3, 4])
        self.slist2 = super_list.SuperList([1, 2])
        self.slist3 = super_list.SuperList(["1", "2"])

    def test_add(self):
        """add test"""
        expected = super_list.SuperList([2, 4, 3, 4])
        self.assertEqual(self.slist1 + self.slist2, expected)

        with self.assertRaises(TypeError):
            self.slist1 + self.slist3

    def test_sub(self):
        """sub test"""
        expected = super_list.SuperList([0, 0, 3, 4])
        self.assertEqual(self.slist1 - self.slist2, expected)

        expected = super_list.SuperList([0, 0, -3, -4])
        self.assertEqual(self.slist2 - self.slist1, expected)

        try:
            self.slist1 - self.slist3
            # "we can't sub str from int"
        except TypeError:
            pass

    def test_diff(self):
        """diff test"""
        self.assertTrue(self.slist1 > self.slist2)

        self.assertFalse(self.slist1 < self.slist2)


if __name__ == "__main__":
    unittest.main()
