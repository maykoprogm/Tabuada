from time import sleep

cores = ['\033[31m', #0 Vermelho
         '\033[32m', #1 Verde
         '\033[33m', #2 Laranja
         '\033[34m', #3 Azul
         '\033[35m', #4 Roxo
         '\033[36m', #5 Azul piscina
         '\033[37m'  #6 Cinza
        ]

def titulo(msg,cor=0):
    tam = len(msg) + 5
    print(cores[cor])
    print('º' * tam)
    print(msg)
    print('º' * tam)
    print('\033[m')

def somar(*num):
    r = sum(num)
    a = f'As somas dos numeros {num} é: {r}'
    return titulo(a,1)

def subtrair(*num):
    if not num:
        return 0
    r = num[0]
    for n in num[1:]:
        r -= n
    a = f'As subtracao dos numeros {num} é: {r}'
    return titulo(a,5)

def multiplicar(*num):
    if not num:
        return 1
    r = 1
    for n in num:
      r *= n
    a = f'A multiplicacao dos numeros {num} é: {r}'
    return titulo(a,2)

def divisao(*num):
    if not num:
        return None
    r = num[0]
    for n in num[1:]:
        r /= n
    a = f'A divisao dos numeros {num} é: {r}'
    return titulo(a,4)


####################### Programa Principal #######################
while True:
    m = '    CALCULADORA MODULAR'
    titulo(m,3)
    entrada = str(input('Digite os números por espaço:  '))
    numeros = entrada.split()
    lista = []
    for n in numeros:
        lista.append(int(n))

    t = input('\nDigite [999] para SAIR ou: '
              '\n+ para somar'
              '\n- para subtrair'
              '\n* para multiplicar'
              '\n/ para dividir'
               '\n: ')

    if t == '999': #Sai do programa.
        break

    elif t not in '+-*/': #Recomeça o programa se não digitar nenhum dos sinais.
        print('\033[31mERRO, recomeçando calculadora..\033[m')
        sleep(1)

    elif t == '+': #Chama a função somar
        somar(*lista)

    elif t == '-': #Chama a função subtrair
        subtrair(*lista)

    elif t == '*': #Chama a função multiplicar
        multiplicar(*lista)

    elif t == '/': #Chama a função dividir
        divisao(*lista)












