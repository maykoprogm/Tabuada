
"""from datetime import date
contador = 0
maioridade = 0
menor = 0
ano_atual = date.today().year


while contador < 7:
     ano = int(input("Qual o ano do seu nascimento?"))
     soma = ano_atual - ano
     contador += 1
     if soma < 18:
         maioridade +=1
     if soma >= 18:
         menor +=1

print('\033[;33m {} pessoas ja atigiram a maioridade.\033[m' .format(maioridade))
print('\033[;36m {} pessoas ainda não atigiram a maioridade.\033[m' .format(menor))"""

"""sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Você digitou errado, tente novamente.\nInforme seu sexo [M/F]: ")).strip().upper()[0]


print("Entendi, seu sexo é {}" .format(sexo))"""



"""from random import randint

computador = randint(1, 10)
contador = 0
print('\033[;;35m JOGO DA ADIVINHACAO\033[m')
print('Tente advinhar qual numero o computador vai escolher de 0 a 10')
jogador = int(input("Numero: "))

while computador != jogador:
     computador = randint(1, 10)
     contador += 1
     print('computador: {}' .format(computador))
     print('Errou, tente de novo.')
     jogador = int(input("Numero: "))

print('Parabens você acertou!')
print('Foram necessarios {} palpites' .format(contador))"""




termo = int(input("Qual o termo da PA? "))
razao = int(input("Qual a razao da PA? "))
contador = 0
PA = termo

while contador < 9 :
    print('{} =>' .format(PA) ,end='')
    contador += 1
    PA += razao



print(PA)