import collections.abc
import math


class Vector(collections.abc.Sequence):
    def __init__(self, val):
        self.value = list(val)

    def addition(self, vect):  # сложение векторов
        if not isinstance(vect, list):
            vect = list(vect)
        if len(self.value) != len(vect):
            raise ValueError("Length of the vectors does not match")

        for i in range(len(self.value)):
            self.value[i] += vect[i]

    def subtraction(self, vect):  # вычитание векторов
        if not isinstance(vect, list):
            vect = list(vect)
        if len(self.value) != len(vect):
            raise ValueError("Length of the vectors does not match")

        for i in range(len(self.value)):
            self.value[i] -= vect[i]

    def mult_const(self, constanta):  # умножение на константу
        for i in range(len(self.value)):
            self.value[i] *= constanta

    def scalar_mult(self, vect):  # xy = x1y1 + x2y2 + ... xn*yn
        if not isinstance(vect, list):
            vect = list(vect)
        if len(self.value) != len(vect):
            raise ValueError("Length of the vectors does not match")

        summ = 0
        for i in range(len(self.value)):
            summ += self.value[i] * vect[i]
        print(summ)

    def equality(self, vect):  # сравнение на равентсво
        if not isinstance(vect, list):
            vect = list(vect)
        if len(self.value) != len(vect):
            raise ValueError("Length of the vectors does not match")

        if self.value == vect:
            return True
        else:
            return False

    def __len__(self):  # получение длинны
        out = 0.0
        for i in range(len(self.value)):
            out += math.pow(self.value[i], 2)
        return math.sqrt(out)

    def __str__(self):  # строковое представление
        return str(self.value)

    def __getitem__(self, key):  # получение элемента по индексу
        elem = self.value[key]
        return elem

    def get_arr(self):
        return self.value


# p1 = Vector([2, -4, 8, 3])
# p_new = Vector([-3, 1, -4, 0])
# p1.subtraction(p_new)
# print(p1)
# p1.__getitem__(2)

p1 = Vector((-2, -1))
p2 = Vector([3, 4])

print(p1)
