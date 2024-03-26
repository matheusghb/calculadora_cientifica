from mathbasi import Mathbasi
from trig import Trigo
num = 0
ope = 0
while (ope != 9):
    print (f'O número atual é: {num}')
    num = float(input("Diga o seu primeiro número: "))
    m = Mathbasi(num)
    t = Trigo(num)
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Exponenciação")
    print ("6 - Raiz")
    print ("7 - Sin, con ou tan")
    print ("8 - Verificar neg")
    print ('9 - Sair')
    ope = int(input("Qual você deseja operar? "))
    if ope==1:
        num = (m.soma())
    if ope==2:
        num = (m.sub())
    if ope==3:
        num = (m.mult())
    if ope==4:
        num = (m.divi())
    if ope==5:
        num = (m.elev())
    if ope==6:
        num = (m.raiz())
    if ope==7:
        esc = input ("Deseja sin, cos ou tan? ")
        if esc == 'sin':
            num = (t.sin())
        if esc == 'cos':
            num = (t.cos())
        if esc == 'tan':
            num = (t.tan())
    if ope==8:
        if (num<0):
            print ("Seu número é negativo. ")
        elif (num>0):
            print ("Seu número não é negativo. ")
        else:
            print ("Seu número é zero. ")
    if ope==9:
        print ("Fechando programa. ")