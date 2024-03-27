import math

class Mathbasi:
    def __init__ (self, num):
        self.num = num

    def soma (self):
        som = float(input("Qual número você deseja somar? "))
        self.num = som + self.num
        return self.num

    def sub (self):
        subt = float(input("Qual número você deseja subtrair? "))
        self.num = self.num - subt
        return self.num

    def divi (self):
        divi = float(input("Qual número você deseja dividir? "))
        self.num = (self.num/divi)
        return self.num

    def  mult (self):
        mult = float(input("Diga o número que deseja multiplicar: "))
        self.num = (self.num*mult)
        return self.num

    def elev (self):
        exp = float(input("Diga o expoente: "))
        nume = self.num
        while (exp > 1):
            self.num = self.num * nume
            exp = (exp-1)
        print (f"O resultado foi {self.num}")
        return self.num

    def raiz (self):
        self.num = math.sqrt(self.num)
        return self.num

    
