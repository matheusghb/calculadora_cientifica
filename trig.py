from mathbasi import Mathbasi
import math

class Trigo(Mathbasi):
    def __init__ (self, num):
        self.num = num

    def sin(self):
        return math.sin(self.num)
    def tan(self):
        return math.tan(self.num)
    def cos(self):
        return math.cos(self.num)