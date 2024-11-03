import unittest
from utils.eval import eval
from utils.show import show

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eval("pre", "+ 3 4"), 7)
        self.assertEqual(eval("pre", "+ * + 3 4 5 7"), 42)
        self.assertEqual(show("pre", "+ 3 4"), "3 + 4")
        self.assertEqual(show("pre", "+ * + 3 4 5 7"), "(3 + 4) * 5 + 7")
        self.assertEqual(eval("post", "3 4 +"), 7)
        self.assertEqual(eval("post", "3 4 5 + 7 * +"), 66)
        self.assertEqual(eval("post", "8 3 - 8 4 4 + * +"), 69)
        self.assertEqual(show("post", "3 4 +"), "3 + 4")
        self.assertEqual(show("post", "8 3 - 8 4 4 + * +"), "8 - 3 + 8 * (4 + 4)")
        self.assertEqual(show("post", "3 4 5 + 7 * +"), "3 + (4 + 5) * 7")
        self.assertEqual(eval("pre", "/ 11 2"), 5)
        self.assertEqual(eval("pre", "+ * * + 3 4 4 5 7"), 147)

        self.assertEqual(eval("mid", "+ 3 4"), None)
        self.assertEqual(eval("pre", "+"), None)
        self.assertEqual(eval("post", "3 4"), None)
        self.assertEqual(show("pre", "3 4"), None)
        self.assertEqual(show("mid", "+ 3 4"), None)
        self.assertEqual(show("pre", "+ 2"), None)
        self.assertEqual(show("post", "+ + 3 4 5"), None)
        self.assertEqual(show("post", "3 4 5"), None)

