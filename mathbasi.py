import math

class Mathbasi:
    def __init__ (self, num):
        self.num = num

    def soma (self):
        som = int(input("Qual número você deseja somar? "))
        self.num = som + self.num
        return print (f"O resultado é {self.num}")

    def sub (self):
        subt = int(input("Qual número você deseja subtrair? "))
        self.num = self.num - subt
        return self.num

    def divi (self):
        divi = int(input("Qual número você deseja dividir? "))
        self.num = (self.num/divi)
        return self.num

    def  mult (self):
        mult = int(input("Diga o número que deseja multiplicar: "))
        self.num = (self.num*mult)
        return self.num

    def elev (self):
        exp = int(input("Diga o expoente: "))
        while (exp > 1):
            self.num = self.num * self.num
            exp = (exp-1)

        return self.num

    def raiz (self):
        self.num = math.sqrt(self.num)
        return self.num

    
