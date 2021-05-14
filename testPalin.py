import unittest
import palin

class TestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(palin.palindrome(),1)
    #Fail Add

if __name__ == '__main__':
    unittest.main()