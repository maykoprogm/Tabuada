# Emprestimo do banco para o comprador da casa

#36
"""casa = float(input("Qual o valor da casa em €? "))
salario = float(input("Qual o seu salario em €? "))
anos = int(input("Em quantos anos voce ira quitar a casa? "))

prestacao = casa / (anos * 12)
if (salario * 0.3) >= prestacao:
    print("Emprestimo concedido com sucesso.")
else:
    print("Emprestimo negado")"""



#37 Conversao de numero para binario,octal ou hexadecimal
"""n = int(input("Digite um numero inteiro: "))
conversao = int(input("Digite o numero correspondente à base de conversao:\n 1 = Binario\n 2 = Octal\n 3 = Hexadecimal?\n"))
binario = hex(n)
if conversao == 1:
    binario = bin(n)
    print("O numero convertido para binario é {}" .format(binario))

elif conversao == 2:
    binario = oct(n)
    print("O numero convertido para octal é {}".format(binario))

elif conversao == 3:
    binario = hex(n)
    print("O numero convertido para hexadecimal é {}".format(binario))
else:
    print("Opcao invalida, tente novamente.")"""



#38
"""n1 = int(input("Digite um numero inteiro qualquer: "))
n2 = int(input("Digite outro numero inteiro qualquer: "))

if n1 > n2:
    print("O primeiro numero é maior que o segundo.")
elif n2 > n1:
    print("O segundo numero é maior que o primeiro.")
else:
    print("Não tem um numero maior, os dois são iguais.")"""


#39 Ja é hora de se alistar?
"""from datetime import datetime as date

ano = int(input("Qual o ano do seu nascimento? "))
ano_atual = date.now().year

if ano_atual - ano <= 17:
    print("Ainda nao esta na hora de se alistar.")
elif ano_atual - ano == 18:
    print("Esta na hora de se alistar")
else:
    print("Ja passou do tempo de se alistar.")"""



#40 Media da nota para saber se passou,esta de recuperação ou reprovou
"""nota1 = float(input("Diga sua primeira nota: "))
nota2 = float(input("Diga sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print("Voce esta Reprovado!")
elif media >= 5.0 and media <= 6.9:
    print("Voce esta de recuperacao")
else:
    print("APROVADO!")"""


#41 Mostrando sua categoria na confederação nacional de natação
"""from datetime import datetime as date

ano = int(input("Qual o ano do seu nascimento? "))
c = date.now().year - ano
if c <= 9:
    print("Sua categoria é MIRIM")
elif c > 9 and c <= 14:
    print("Sua categoria é INFANTIL")
elif c > 14 and c <=19:
    print("Sua categoria é JUNIOR")
elif c == 20:
    print("Sua categoria é SENIOR")
else:
    print("Sua categoria é MASTER")"""



#42 Mostrando se é possivel formar um triangulo e qual tipo de triangulo: equilatero, isosceles ou escaleno.
"""print("Quer saber se é possivel formar um triangulo e qual o tipo?\n")
lado1 = float(input("Digite em centimetros o segmento do primeiro lado: "))
lado2 = float(input("Digite em centimetros o segmento do segundo lado: "))
lado3 = float(input("Digite em centimetros o segmento do terceiro lado: "))
triangulo = lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2

if triangulo and lado1 == lado2 == lado3:
    print("Sim, é possivel formar um triangulo com esses valores de segmentos e é um triangulo Equilatero.")
elif triangulo and lado1 == lado2 != lado3 or lado3 == lado2 != lado1 or lado1 == lado3 != lado2:
    print("Sim, é possivel formar um triangulo com esses valores de segmentos e é um triangulo Isóceles.")
elif triangulo and lado1 != lado2 != lado3:
    print("Sim, é possivel formar um triangulo com esses valores de segmentos e é um triangulo Escaleno.")
else:
    print("Não é possivel formar um traingulo")"""



#43 Calculando seu IMC
"""peso = float(input("Digite o seu peso: "))
alt = float (input("Digite sua altura(metros): "))
imc = peso / (alt**2)

if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Voce esta no peso ideal.")
elif imc > 25 and imc <= 30:
    print("Voce esta com sobrepreso")
elif imc > 30 and imc <=40:
    print("Voce esta com obesidade")
else:
    print("Voce esta com obesidade morbida.")"""



#44 Calculando o valor a ser pago do produto com descontos ou acréscimos
"""print('{:=^40}' .format ("LOJA DO MAYKO"))
p = float(input("Qual o preco do produto? "))
print("Qual a forma de pagamento?")
fp = int(input("Digite\n 1 = à vista em dinheiro/chque\n 2 = à vissta no cartao\n 3 = 2x no cartao\n 4 = 3x ou mais no cartao\n "))

if fp == 1:
    preco = p - (p*0.1)
    print("O valor à ser pago é {}" .format(preco))
elif fp ==2:
    preco = p - (p*0.05 )
    print("O valor à ser pago é {}".format(preco))
elif fp == 3:
    preco = p
    print("O valor à ser pago é {}".format(preco))
elif fp == 4:
    preco = p + (p * 0.2)
    print("O valor à ser pago é {}".format(preco))"""



#45
from random import randint
print('{:=^40}' .format (" Bem vindo ao jogo do Jokenpô "))
a = int(input("Escolha entre\n 0= pedra\n 1 = papel\n 2 = tesoura\n "))
print(" JO\n KEN \n PO\n")
opcoes = ('pedra','papel','tesoura')
computador = randint(0,2)
print('*' * 20)
print("computador escolheu {} " .format(opcoes[computador]))
print("Voce escolheu {}" .format(opcoes[a]))
print('*' * 20)

if computador == 0 and a == 2 or computador == 1 and a == 0 or computador == 2 and a == 1:
    print("Voce perdeu.")
elif computador == 0 and a == 1 or computador == 1 and a == 2 or computador == 2 and a == 0:
    print("Voce ganhou.")
elif computador == 0 and a == 0 or computador == 1 and a == 1 or computador == 2 and a == 2:
    print("Empate!")





