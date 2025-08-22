# 28
import random
"""r = random.randint(0,5) # Escolher um numero entre 0 e 5
n = int(input("Qual numero foi escolhido pelo computador? "))
if n == r:
    print("Você venceu")
else:
    print("Você perdeu")
    print("O computador escolheu o numero {} " .format(r))"""


#29
"""vel = int(input("Qual a velocidade do carro? "))
multa = (vel - 80) * 7
if vel >=81:
    print("O carro foi multado.")
    print("A multa custara {} reais." .format(multa))"""



#30
"""n = int(input("Digite um numero inteiro "))
if n%2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")"""


#31
"""km = float(input("Qual a distancia da sua viagem em KM? "))
kmbaixa = 0.50 * km
kmalta = 0.45 * km
if km <= 200:
    print("Sua viagem custara {}" .format(kmbaixa))
else:
    print("Sua viagem custara {}" .format(kmalta))"""



#32
"""ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} é bissexto" .format(ano))
else:
    print("O ano {} não é bissexto" .format(ano))"""



#33
"""n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o primeiro numero: "))
n3 = int(input("Digite o primeiro numero: "))

menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n2 and n3<n1:
    menor= n3
print("O menor numero é o {}" .format(menor))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("O maior numero é {}" .format(maior))"""





#34
"""salario = float(input("Qual o seu salario em Euro? "))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.1)
print("O seu novo salario é {}" .format(novo))"""




#35
"""c1 = float(input("Digite o comprimento da reta 1: "))
c2 = float(input("Digite o comprimento da reta 2: "))
c3 = float(input("Digite o comprimento da reta 3: "))

if (c1 + c2 > c3) and (c1 + c3 >c2) and (c2 + c3 > c1):
    print("As 3 retas formam um triangulo")
else:
    print("As 3 retas não formam um triangulo")"""




