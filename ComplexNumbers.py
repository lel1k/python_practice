from math import sqrt


class ComplexNumber:
    def __init__(self, real, Im):
        self.real = real
        self.Im = Im

    def sum(self, second_number):
        return ComplexNumber(self.real + second_number.real, self.Im + second_number.Im)

    def sub(self, second_number):
        return ComplexNumber(self.real - second_number.real, self.Im - second_number.Im)

    def mul(self, second_number):
        return ComplexNumber(self.real * second_number.real - self.Im * second_number.Im, \
                             self.real * second_number.Im + self.Im * second_number.real)

    def mod(self):
        return sqrt(self.real ** 2 + self.Im ** 2)

    def copy(self):
        return ComplexNumber(self.real, self.Im)

    def comparison(self, second_number):
        operation_success = False
        if self.Im == second_number.Im and self.real == second_number.real:
            operation_success = True
        return operation_success
