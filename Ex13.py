#57
"""sexo = str(input("Qual o seu sexo? ")).upper()[0].strip()
while sexo !='M' and sexo !='F':    #OU while sexo not in 'MmFf'
    sexo = str(input("Dados invalidos, por favor informe seu sexo?:")).upper()[0].strip()
print("FIM")"""
from dataclasses import replace

#58
"""import random

computador = random.randint(0,10)

print('{:^100}' .format ('\033[;;43m COMPUTADOR PENSANDO EM UM NÚMERO ENTRE 0 E 10 ...\033[m'))
numero = int(input("\nQual o numero que o computador pensou?  "))

while computador != numero:
    print("ERROU, TENTE NOVAMENTE")
    numero = int(input('Qual o numero?? '))
    

print("PARABENS VOCÊ CONSEGUIU!")
print('Computador tambem escolheu o numero {}' .format(computador))"""



#59
"""n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
menu = 0


while menu != 5:
      #{:=^40}' .format
      print(
            "\n[1] SOMAR\n"
            "[2] MULTIPLICAR\n"
            "[3] NUMERO MAIOR\n"
            "[4] NOVOS NUMEROS\n["
            "5] SAIR DO PROGRAMA")
      menu = int(input("\033[;36mEscolha uma opção:\033[m"))
      if menu == 1:
          print(n1 + n2)

      elif menu == 2:
          print(n1 * n2)

      elif menu == 3:
          if n1 > n2:
              print(n1)
          else:
              print(n2)

      elif menu == 4:
          n1 = int(input("Digite um valor: "))
          n2 = int(input("Digite outro valor: "))

      elif menu == 5:
          print("Saindo do programa...")

      else:
          print('Opção invalida.')
print('Fim do programa, volte sempre!')"""




#60 FATORIAL
import math
"""print('{:=^100}' .format ('\033[1;32m PROGRAMA QUE MOSTRA O FATORIAL DO NUMERO DIGITADO\033[m'))
numero = int(input("Digite um numero inteiro: "))

fatorial = math.factorial(numero)
print(fatorial)"""

# ====== OR ======
"""print('{:=^100}' .format ('\033[1;32m PROGRAMA QUE MOSTRA O FATORIAL DO NUMERO DIGITADO\033[m'))
numero = int(input("Digite um numero inteiro: "))

contador = numero
fatorial = 1

print('Calculando {}! =  ' .format(numero),end='')

while contador > 0:
    print('{}'. format(contador), end = '')
    print(' x ' if contador > 1 else print('='), end = '')
    fatorial *= contador
    contador -= 1
print(' o fatorial de {} é {}' .format(numero,fatorial))"""

# ========== OR =============

"""print('{:=^100}' .format ('\033[1;32m PROGRAMA QUE MOSTRA O FATORIAL DO NUMERO DIGITADO\033[m'))
n = int(input("Digite um numero inteiro: "))

fatorial = 1
numero = n


for c in range (1,n +1):
    print(c,end='')
    print('x' if c < n else print('= {}' .format(fatorial)),end='')
    fatorial *= numero
    numero -= 1
print("o resultado é {}" .format(fatorial))"""


#61 PROGRESSAO ARITMETICA COM WHILE
"""print('\033[36m QUER SABER A PROGRESSÃO ARITMÉTICA DE UM NÚMERO?\033[m')
termo = int(input("Digite o termo da PA: "))
razao = int(input('Digite a razao da PA:  '))

contador = 1
soma = termo



while contador < 11:
      print('{}' .format(soma),end='')
      print(',' if contador < 10 else '.',end='')
      contador += 1
      soma += razao"""



#63 SEQUENCIA DE FIBONACCI
from sympy import fibonacci
"""n = int(input("Quantos elementos da sequência de Fibonnaci você quer ver?"))
contador = 0
t1 = 0
t2 = 1
print('{},{},' .format(t1, t2),end='')

while contador <= n:
    t3 = t1 + t2
    print('{},'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1"""


#64
"""print('\033[1;34m-\033[m'* 55)
print('\033[1;34mTente advinhar o numero secreto para o programa parar.\033[m')
print('\033[1;34m-\033[m'*55)
n = 0
contador = 0
soma = n

while n != 999:
    n = int(input("Digite um numero inteiro: "))
    contador += 1
    soma += n
    

print('Foram digitador {} numeros' .format(contador))

print('E a soma deles é {}' .format(soma - 999))"""


#65
"""saida = 1
num = contador = maior = menor = 0
soma = num


print('\033[;33mEste programa no final vai mostrar a média dos numeros digitados e o maior e menor valor lido.\033[m')

while saida == 1:
   num = int(input("Digite um numero: "))
   contador += 1
   if contador == 1:
       maior = menor = num
   else:
       if num > maior:
           maior = num
       if num < menor:
           menor = num
   soma += num

   saida = int(input("Digite [1] para continuar e [2] para sair: \n"))



media = soma / contador
print('\nA média entre todos os valores digitados é {:.1f}' .format(media))
print('O maior número é o {}' .format(maior))
print('O menor número é o {}' .format(menor))


print('FIM')"""










