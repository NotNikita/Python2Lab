from task4 import func
import unittest


class DecoratorTest(unittest.TestCase):

    def test_f(self): # testing kwargs
        func(Hello=100, World = 200)
        self.assertEqual(func(Hello=100, World = 200), func(Hello=100, World = 200))

    def test_f2(self): #testing memorizing
        self.assertEqual(func(5,2,3,4), func(5,2,3,4))

    def test_f3(self): #testing args
        self.assertEqual(func(5, Hello_Dolly = 1, Hello_World =2), func(5, Hello_Dolly = 1, Hello_World =2))


if __name__ == '__main__':
    unittest.main()