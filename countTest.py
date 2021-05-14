import unittest
import count

class TestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(count.count(),2)
    def test_false(self):
        self.assertEqual(count.count(),3)

if __name__ == '__main__':
    unittest.main()