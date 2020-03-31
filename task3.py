import math


class Vector:
    value = []

    def __init__(self, value):
        self.value = value

    def info(self):
        print(self.value)

    def addition(self, vect2):
        if len(self.value) != len(vect2.value): print("sizes are not equal")
        for i in range(len(self.value)):
            self.value[i] += vect2.value[i]

    def subtraction(self, vect):
        if len(self.value) != len(vect.value): print("sizes are not equal")
        for i in range(len(self.value)):
            self.value[i] -= vect.value[i]

    def mult_const(self, constanta):
        for i in range(len(self.value)):
            self.value[i] *= constanta

    def scalar_mult(self, vect):  # xy = x1y1 + x2y2 + ... xn*yn
        if len(self.value) != len(vect.value): print("sizes are not equal")
        sum = 0
        for i in range(len(self.value)):
            sum += self.value[i] * vect.value[i]
        print(sum)

    def equality(self, vect2):
        if self.value == vect2.value:
            print("These 2 vectors are equal")
        else:
            "These 2 vectors are NOT equal"

    def length(self):
        out = 0
        for i in range(len(self.value)):
            out += math.pow(self.value[i], 2)
        return math.sqrt(out)

    def __str__(self):
        out_str = '('
        for i in range(len(self.value)):
            out_str += '%d,' % (self.value[i])
        out_str = out_str[:len(out_str) - 1]
        return out_str + ')'


p2 = Vector([2, -4, 8, 3])

print(p2)
