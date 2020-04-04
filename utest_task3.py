import task3
import unittest
import math


class VectorTest(unittest.TestCase):

    def test_add(self, v1=task3.Vector([2, -4, 8, 3]), v2=task3.Vector([-3,1,-4,0])):
        v1.addition(v2)
        self.assertEqual(v1.get_arr(), [-1,-3,4,3])

    def test_sub(self, v1=task3.Vector([2, -4, 8, 3]), v2=task3.Vector([-3,1,-4,0])):
        v1.subtraction(v2)
        self.assertEqual(v1.get_arr(),[5,-5,12,3])

    def test_mult_const(self, v1=task3.Vector([2, -4, 8, 3]), const=2):
        v1.mult_const(const)
        arr = v1.get_arr()
        for i in arr:
            i=i*2
        self.assertEqual(v1.get_arr(),arr)

    def test_equality(self, v1=task3.Vector([2, -4, 8, 3]), v2=task3.Vector([-3,1,-4,0])):
        self.assertFalse(v1.equality(v2))

    def test_length(self, v1=task3.Vector([2, -4, 8, 3])):
        v1_arr = v1.get_arr()
        out = 0.0
        for i in v1_arr:
            out += math.pow(i, 2)

        self.assertEqual(v1.length(), math.sqrt(out))

    def test_get_elem(self, v1=task3.Vector([2, -4, 8, 3]), elem = 2):
        self.assertEqual(v1.get_elem(elem), v1.get_arr()[elem])


if __name__ == '__main__':
    unittest.main()