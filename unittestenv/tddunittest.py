import unittest


def multiplyall(a, b):
    return a*b


class TestMultiplyAll(unittest.TestCase):

    def test_multiplyall1(self):
        self.assertEqual(multiplyall(1, 1), 1)
        self.assertEqual(multiplyall(-1, 1), -1)
        self.assertEqual(multiplyall(-1, -1), 1)

    def test_multiplyall2(self):
        self.assertEqual(multiplyall(2, 2), 4)
        self.assertEqual(multiplyall(-2, 2), -4)
        self.assertEqual(multiplyall(-2, -2), 4)

    def test_multiplyall3(self):
        self.assertEqual(multiplyall(3, 3), 9)
        self.assertEqual(multiplyall(-3, 3), -9)
        self.assertEqual(multiplyall(-3, -3), 9)

    def test_multiplyall4(self):
        self.assertEqual(multiplyall(41, 14), 41*14)
        self.assertEqual(multiplyall(-41, 14), -41*14)
        self.assertEqual(multiplyall(-41, -14), 41*14)


if __name__ == '__main__':
    unittest.main()
