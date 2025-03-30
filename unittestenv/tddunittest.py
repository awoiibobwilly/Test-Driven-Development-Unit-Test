import unittest


def multiplyall(a, b):
    return a*b


class TestMultiplyAll(unittest.TestCase):

    def test_multiplyall1(self):
        self.assertEqual(multiplyall(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
