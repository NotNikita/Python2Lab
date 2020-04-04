import task4
import unittest


class DecoratorTest(unittest.TestCase):

    def test_f(self):
        self.assertNotEqual(task4.f(4), 0)

    def test_f2(self):
        self.assertEqual(task4.f(5), task4.f(5))

    def test_f3(self):
        self.assertNotEqual(task4.f(5), task4.f(2))


if __name__ == '__main__':
    unittest.main()