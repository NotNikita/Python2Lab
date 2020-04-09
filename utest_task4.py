from task4 import func
import unittest


class DecoratorTest(unittest.TestCase):

    def test_f(self): # testing kwargs
        func(Hello=100, World = 200)
        self.assertNotEqual(func('Hello'), 100)

    def test_f2(self): #testing memorizing
        self.assertEqual(func(5), func(5))

    def test_f3(self): #testing args
        func(1,5,10,15,20)
        self.assertNotEqual(func(5), func(10))


if __name__ == '__main__':
    unittest.main()