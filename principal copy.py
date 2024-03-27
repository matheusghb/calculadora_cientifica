# copy()
# replace()
# rsplit()

import math
ope = 0
his = []

while (ope != 4):
    print ("1 - Iniciar")
    print ("2 - Histórico")
    print ("3 - Apagar histórico")
    print ("4 - Sair")
    ope = int(input ("-> "))
    if ope == 1:
        print ("Diga a expressão que deseja utilizar. ")
        print ("+ Soma, - Subtrái, * multiplica, / divide (// divide inteiro);")
        print ("** eleva, () isola, math.sqrt() raiz")
        print ("math. sin, cos ou tan vai dar o número correspondente. ")
        print ("math.pi resultará em pi. ")
        num = input("-> ")
        nume = eval(num)
        print (f"O resultado é {nume}. ")
        his.append(f"{num} que foi igual a {nume}. ")
        print (f"Sin é: {math.sin(nume)}")
        print (f"Cos é: {math.cos(nume)}")
        print (f"Tan é: {math.tan(nume)}")
    elif ope == 2:
        print (his[:])
    elif ope == 3:
        his.clear()
    elif ope == 4:
        print ("Fechando programa. ")
    else:
        print ("Ocorreu um erro. ")