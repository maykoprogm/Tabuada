 # Comando BREAK para a repetição.

#66
"""contador = soma =0
print(f'\033[42m {'Bem-vindo ao programa! Se quiser sair do programa,digite 999.'}\033[m\n')

while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma +=num
    contador += 1

print(f'\nForam digitados {contador} números \nE a soma entre eles é {soma}\n')
print(f'\033[35m {' FIM ':=^70}\033[m')"""


 #67 TABUADA
"""resultado = 0

print(f'\033[42m{'=':=^40}\033[m')
print(f'\033[44m{'TABUADA DO MAYKO ':=^40}\033[m')
print(f'\033[43m{'=':=^40}\033[m')

while True:
   cont = 0
   num = int(input("\nQuer ver a tabuada de qual número? " '\n Digite [9999] para SAIR \n'))

   if num < 0 or num == 9999:
       break

   while cont < 10:
      cont += 1
      resultado = num * cont
      print(f'{num} x {cont} = {resultado}')


print('Programa finalizado.')"""


#68
"""from random import randint

vitoria = 0

while True:
   jogador = int(input('\nDigite um numero: '))
   computador = randint(1,10)
   total = jogador + computador
   tipo = ' '

   while tipo not in 'PI':
     tipo = str(input('Você quer Par ou Ímpar? ')).strip().upper()[0]
     print(f'\nVocê jogou {jogador} e o computador jogou {computador} = {total}')

   if tipo == 'P':
       if total % 2 == 0:
         print('Você \033[32mGANHOU\033[m esta rodada!')
         vitoria += 1
       else:
           print('\033[35mGAME OVER!!\033[m')
           print(f'Você venceu {vitoria} vezes.')
           break

   elif tipo == 'I':
       if total % 2 != 0:
         print('Você \033[32mGANHOU\033[m esta rodada!')
         vitoria += 1
       else:
           print('\033[35mGAME OVER!!\033[m')
           print(f'Você venceu {vitoria} vezes.')
           break
   print('Vamos jogar novamente...')"""




#69
"""mensagem = '*  CADASTRANDO PESSOA  *'
print(f'\033[33m{mensagem:^60}\033[m')

c_idade = c_homem = c_mulher = 0

while True:
     idade = int(input('Digite a Idade: '))
     sexo = ' '

     while sexo not in 'fFmM':
         sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
     if idade >= 18:
         c_idade += 1
     if sexo in 'M':
         c_homem += 1
     if sexo in 'F' and idade < 20:
         c_mulher += 1

     continuar = ' '
     while continuar not in 'SN':
         continuar = str(input(f'{' Quer continuar?[S/N]':=>32}')).upper().strip()[0]
     if continuar == 'N':
         break



print(f'{c_idade} pessoas tem mais de 18 anos.')
print(f'{c_homem} homens foram cadastrados.')
print(f'{c_mulher} mulheres tem menos de 20 anos.')"""





#70
"""gasto = produto_mais = cont  = barato =0
nome_barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preco do Produto: R$ '))
    gasto += preco
    cont += 1

    if preco > 1000:
        produto_mais += 1

    if cont == 1 or preco < barato:
        barato = preco
        nome_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break



print(f'O total gasto foi R${gasto}')
print(f'{produto_mais} custam mais que R$1000')
print(f'O nome do produto mais barato foi o {nome_barato} e custou {barato}')"""



#71

valor = int(input('Qual o valor que deseja sacar? '))
ced = 50
total = valor
cont = 0
while True:
  if total >= ced:
      total -=ced
      cont += 1
  else:
      if






print(total)
print(cont)