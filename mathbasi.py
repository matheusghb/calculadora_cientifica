import math

class Mathbasi:
    def __init__ (self, num):
        self.num = num

    def soma (self):
        som = int(input("Qual número você deseja somar? "))
        return (som + self.num)

    def sub (self):
        subt = int(input("Qual número você deseja subtrair? "))
        return (self.num - subt)

    def divi (self):
        divi = int(input("Qual número você deseja dividir? "))
        return (self.num/divi)

    def  mult (self):
        mult = int(input("Diga o número que deseja multiplicar: "))
        return (self.num * mult)

    def elev (self):
        exp = int(input("Diga o expoente: "))
        while (exp > 1):
            self.num = self.num * self.num
            exp = (exp-1)

        return self.num

    def raiz (self):
        return math.sqrt(self.num)

    
