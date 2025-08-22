#nome = input("Digite seu nome: ")
#print ("Seja Bem Vindo,",nome)
#print ("Seja Bem Vindo {:=^20}!".format(nome))

# /n continua a linha na linha de baixo e end="" continua na mesma linha

# n1 = int(input("Digite um numero: "))
# n2 = input("Digite um segundo numero: ")
# print(type(n1))
# print(type(n2))

# n = input("Digite um numero: ")
# print(n.isnumeric())

#a = input("Digite algo: ")
#print("Qual o tipo:" , type(a))
#print("Tem espaço?" ,a.isspace())
#print("É um numero" ,a.isnumeric())
#print(" É alfabetico?" ,a.isalpha())
#print(a.isalnum())
#print(a.isupper())
#print(a.islower())

####  EXERCICIOS  da aula NUMERO 7  ex:7 ~ 15.

"""n = int(input("Digite um numero: "))
an = n - 1
su = n + 1
print ("O numero é {}, seu antecessor é {} e o seu sucessor é {}" .format(n,an,su)) """
from functools import total_ordering

"""n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
m = (n1 + n2) / 2
print("A Media é {:.1f}" .format(m))"""



"""metros = int(input("Digite um valor em Metros:"))
cen = metros * 100
mili = metros * 1000
print("O valor convertido em Centi é {} e o valor em Mili é {} " . format(cen,mili))"""



"""d = float(input("Digite quanto voce tem em dinheiro: "))
c = d / 3.27
print("Você pode comprar {:.2f} dolares" .format(c))"""


"""la = float(input("Digite a largura em metros: "))
al = float(input("Digite a altura em metros : "))
area = (la * al)
t = (la * al) / 2
print("Sua area total é {}, e a quantidade de tinta necessaria é {} litros. ". format(area,t))"""


"""p = float(input("Digite o preco do produto: "))
np = (p*5) / 100
total = p - np
print(" O novo preço custa: {:.2f}" .format(total))"""


"""s = float(input("Qual o salario do funcionario? R$"))
total = ((s * 15 )/100) + s
print("O funcionario ganhava {} e com o aumento de 15%, agora ganha {:.2f}" . format(s,total))"""


"""c = float(input(" Informe a temperatura em Celsius"))
f = (c*1.8) + 32
print(" A temperatura em fahrenheit é {}" . format(f))"""


d = int(input("Quantos dias alugados? "))
km = int(input("Quantos KM rodados? "))
t = (d * 60.) + (km * 0.15)
print("O total a pagar é {}" .format(t))



