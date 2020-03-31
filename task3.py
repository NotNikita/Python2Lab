import math


class Vector:
    value = []

    def __init__(self, value):
        self.value = value


    def addition(self, vect2): # сложение векторов
        if len(self.value) != len(vect2.value): print("sizes are not equal")
        for i in range(len(self.value)):
            self.value[i] += vect2.value[i]

    def subtraction(self, vect): # вычитание векторов
        if len(self.value) != len(vect.value): print("sizes are not equal")
        for i in range(len(self.value)):
            self.value[i] -= vect.value[i]

    def mult_const(self, constanta): # умножение на константу
        for i in range(len(self.value)):
            self.value[i] *= constanta

    def scalar_mult(self, vect):  # xy = x1y1 + x2y2 + ... xn*yn
        if len(self.value) != len(vect.value): print("sizes are not equal")
        sum = 0
        for i in range(len(self.value)):
            sum += self.value[i] * vect.value[i]
        print(sum)

    def equality(self, vect2): # сравнение на равентсво
        if self.value == vect2.value:
            print("These 2 vectors are equal")
        else:
            "These 2 vectors are NOT equal"

    def length(self): # получение длинны
        out = 0
        for i in range(len(self.value)):
            out += math.pow(self.value[i], 2)
        return math.sqrt(out)

    def __str__(self): # строковое представление
        out_str = '('
        for i in range(len(self.value)):
            out_str += '%d,' % (self.value[i])
        out_str = out_str[:len(out_str) - 1]
        return out_str + ')'

    def get_elem(self, num): # получение элемента по индексу
        print(num," element in vector is", self.value[num])


p1 = Vector([2, -4, 8, 3])
p_new = Vector([-3, 1, -4, 0])

p1.addition(p_new)
print(p1)
p1.get_elem(2)
