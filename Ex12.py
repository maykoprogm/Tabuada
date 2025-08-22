#46 CONTAGEM REGRESSIVA
"""print("Contagem regressiva para o estouro dos fogos de artificios!")
soma = 0
for c in range(10,0,-1):
    print(c)
print("!@#!%@#!@ BOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM! @#!@$%#%")"""


#47
"""for pares in range(2,51,2):
    print(pares)"""


#48
"""for impar in range (0,500,3):
    print(impar)
#ou

for impar in range(0,500):
    if impar % 3 == 0:
       print(impar)"""


#49
"""numero = int(input("Digite um numero para  ver a tabuada dele: "))
i=1
while i <=10:
    for c in range(0,10):
        print("{} x {} = {}" .format(numero,i,numero*i))
        i += 1"""


#50
"""soma = 0
cont = 0
for c in range(1,7):
  num = int(input("Digite o {} numero: " .format(c)))
  if num % 2 ==0:
   soma += num
   cont += 1
print("voce informou {} numeros e a soma foi {} " .format(cont,soma))"""



#51 PROGRESSAO ARITMETICA
"""primeiro_termo = int(input("Digite o primeiro termo da progressao aritmetica: "))
razao = int(input("Digite a razao: "))
decimo = primeiro_termo + (10 * razao)
for c in range (primeiro_termo,decimo,razao):
 print(c, end = ' --')"""



#52 DESCOBRINDO SE O NUMERO É PRIMO OU NÃO
"""print('=' * 70)
print('{:^70}'.format ("\033[;34m Quer saber se algum numero inteiro é primo?\033[m"))
print('=' * 70)
numero = int(input("Digite um numero inteiro: "))
total = 0
total1 = 0

for c in range (1, numero + 1):
    if numero % c == 0:
        print("{}" .format(c),end=' ')
        total += 1

    elif numero % c != 0:

        total1 += 1

print("\nO numero {} foi dividido {} vezes" .format(numero,total))

if total == 2:
  print("É PRIMO!")

else:
    print("NÃO É PRIMO!")"""




#53
"""print(('{:^110}'.format ("\033[;33m Digite uma frase para ver se é uma frase Palindromo: \033[m ")))
frase = str(input("frase:")).upper()
sem_espacos = frase.replace(' ', '')

if sem_espacos == sem_espacos[::-1]:
    print("A frase é um Palindromo: {}" .format(sem_espacos[::-1]))
else:
    print('Não é um Palindromo: {}' .format(sem_espacos[::-1]))"""


# APENAS MOSTRANDO COMO SEPARAR E JUNTAR.
"""s = str(input("Digite uma frase"))
separar = s.split()
print(separar)
juntar = ''.join(separar)
print(juntar)"""




#54 CALCULANDO SE A PESSOA É MAIORIDADE OU NAO
"""from datetime import date

data_atual= date.today().year
print("\033[4;31m Estamos no ano de {} \033[m\n" .format(data_atual))
total = 0
total1 = 0
a = 1
for c in range(1,8):
    ano = int(input(" - Qual o ano a {} pessoa nasceu? " .format(a)))
    a += 1
    if data_atual - ano >= 18:
        total += 1

    else:
        total1 += 1
print("\033[;;42m {} pessoas ja atingiram a MAIORIDADE \033[m" .format(total))
print("\033[;;41m {} pessoas NÃO ATINGIRAM A MAIORIDADE \033[m" .format(total1))"""



#55 MOSTRANDO QUAL O MAIOR E QUAL O MENOR PESO ENTRE 5 PESSOAS
"""lista = []

for c in range (1,6):
    peso = float(input("Qual o peso da {} pessoa? " .format(c)))
    lista.append(peso) #ADD na lista

maior = max(lista)
menor = min(lista)
print("O \033[;;42m MAIOR \033[m peso lido foi {}" .format(maior))
print("O \033[;;41m MENOR \033[m peso lido foi {}" .format(menor))"""



#56
mais_velho = ''
maioridade_homem = 0
soma_idade = 0
mulheres = 0
for c in range (1,6):

    print(" °°°° {}ª PESSOA °°°° " .format(c))
    nome = str(input(" NOME: ")).strip()
    idade = int(input(' IDADE: '))
    sexo = str(input(' SEXO [M/F]: ')).strip()
    soma_idade += idade

# Primeiro if é para ,na primeira pessoa que for homem, inicializa as variaveis com idade e nome dessa pessoa.
# Para se ter uma comparação com as proximas pessoas do sexo M
    if c == 1 and sexo in 'Mm':
        maioridade_homem = idade
        mais_velho = nome

# No 2º if, se for um homem mais velho do que o armazenado, ele substitui os valores nome e a idade.
    if sexo in 'mM' and maioridade_homem < idade:
        maioridade_homem = idade
        mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulheres += 1



media = soma_idade / 2
print('A \033[;32m média de idade\033[m do grupo é {}' .format(media))
print('O \033[;33m homem mais velho\033[m tem {} anos e se chama {}' .format(maioridade_homem,mais_velho))
print('{}  mulheres \033[;34m tem menos de 20\033[m' .format(mulheres))







