import unittest
from descriptor import Data
from meta import CustomClass


class TestClass(unittest.TestCase):
    def test_descriptor(self):
        data = Data(-1, "str", 14)
        self.assertTrue((-1, "str", 14 == data.get_values()))
        self.assertRaises(Exception, Data, 0.54, "str", 1)
        self.assertRaises(Exception, Data, 0, set(), 1)
        self.assertRaises(Exception, Data, 0, "str", -90)
        self.assertRaises(Exception, Data, 0, "str", "str")

    def test_meta(self):
        cc = CustomClass()
        cc.custom_print()
        #print(dir(cc))
        self.assertEqual(cc.custom_get_x(), 50)
        self.assertEqual(cc.custom_get_val(), 99)
        try:
            cc.print()
        except AttributeError:
            pass 


if __name__ == "__main__":
    unittest.main()
