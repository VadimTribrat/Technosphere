import unittest
from lru import LRU


class TestClass(unittest.TestCase):
    def test_1(self):
        cache = LRU(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertTrue(cache.get("k3") is None)
        self.assertTrue(cache.get("k2") == "val2")
        self.assertTrue(cache.get("k1") == "val1")
        cache.set("k3", "val3")
        self.assertTrue(cache.get("k3") == "val3")
        self.assertTrue(cache.get("k2") is None)
        self.assertTrue(cache.get("k1") == "val1")

    def test_2(self):
        cache = LRU(2)
        cache.set("k1", "val1")
        cache.set("k1", "val2")
        self.assertTrue(cache.get("k3") is None)
        self.assertTrue(cache.get("k2") is None)
        self.assertTrue(cache.get("k1") == "val2")
        cache.set("k3", "val3")
        self.assertTrue(cache.get("k3") == "val3")
        self.assertTrue(cache.get("k2") is None)
        self.assertTrue(cache.get("k1") == "val2")
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertTrue(cache.get("k2") == "val2")
        self.assertTrue(cache.get("k3") is None)
        self.assertTrue(cache.get("k1") == "val1")

    def test_3(self):
        cache = LRU(1)
        self.assertTrue(cache.get("k1") is None)
        cache.set("k1", "val1")
        self.assertTrue(cache.get("k1") == "val1")
        cache.set("k1", "val2")
        self.assertTrue(cache.get("k1") == "val2")
        cache.set("k2", "val2")
        self.assertTrue(cache.get("k2") == "val2")
        self.assertTrue(cache.get("k1") is None)

    def test_4(self):
        cache = LRU(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertTrue(cache.get("k1") == "val1")
        self.assertTrue(cache.get("k2") == "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertTrue(cache.get("k3") == "val3")
        self.assertTrue(cache.get("k4") == "val4")
        self.assertTrue(cache.get("k1") is None)
        self.assertTrue(cache.get("k2") is None)

    def test_5(self):
        cache = LRU(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        self.assertTrue(cache.get("k1") == "val1")
        self.assertTrue(cache.get("k2") == "val2")
        self.assertTrue(cache.get("k3") == "val3")
        cache.set("k1", "val11")
        cache.set("k4", "")
        self.assertTrue(cache.get("k2") is None)
        cache.set("k5", "")
        self.assertTrue(cache.get("k2") is None)
        self.assertTrue(cache.get("k3") is None)
        cache.set("k6", "")
        self.assertTrue(cache.get("k1") is None)
        self.assertTrue(cache.get("k2") is None)
        self.assertTrue(cache.get("k3") is None)
        self.assertTrue(cache.get("k4") == "")
        self.assertTrue(cache.get("k5") == "")
        self.assertTrue(cache.get("k6") == "")


if __name__ == "__main__":
    unittest.main()
