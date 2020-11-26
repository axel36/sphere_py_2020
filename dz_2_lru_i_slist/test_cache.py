"""tests"""
import unittest
from dz_2_lru_i_slist import cache


class CacheTestCase(unittest.TestCase):
    """cache tests"""

    def setUp(self):
        self.cache = cache.LRUCache(10)
        for i in range(10):
            self.cache.set(str(i), str(i + 10))

    def test_main(self):
        """main logic test"""

        self.assertEqual(self.cache.get("2"), "12")

        self.assertEqual(len(self.cache._keys), 10)
        self.cache.delete("4")
        self.assertEqual(len(self.cache._keys), 9)
        self.assertIsNone(self.cache.get("4"))

    def test_capacity(self):
        """capacity test"""
        self.assertIsNone(None)
        for i in range(10):
            # self.assertEqual(self.cache.get(str(i)), str(i + 10))
            self.cache.set(str(i + 100), str(i + 100))
            self.assertIsNone(self.cache.get(str(i)))
        self.assertEqual(self.cache.get("109"), "109")

    def test_set(self):
        """update value test"""
        self.assertEqual(self.cache._storage["9"], "19")
        self.cache.set("9", "str")
        self.assertEqual(self.cache._storage["9"], "str")
        self.cache.set("9", "str2")
        self.assertEqual(self.cache.get("9"), "str2")


if __name__ == "__main__":
    unittest.main()
