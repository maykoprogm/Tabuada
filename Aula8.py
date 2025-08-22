# import bebida -- importa a biblioteca toda
# from bebida import cafe -- importa apenas o cafe da biblioteca bebida
""" BIBLIOTECAS
math (funções matematicas)
random (numero aleatorios) # gera um número aleatorio
datetime (datas e horarios)
json (ler e salvar dados em JSON)
numpy (calculos numericos e matrizes)
pandas (análise de dados e tabelas dataframe)
pygame (criar jogos) 
trunc ( pega a parte inteira do numero)
math.raians ( converte graus em radianos)
"""


import math
import random
import emoji
import pygame

"""n = int(input("Digite um numero: "))
raiz = math.sqrt(n)
print("A raiz quadrada de {} é {}" .format (n,math.ceil(raiz))) # ceil arredonda para cima
print("A raiz quadrada de {} é {}" .format (n,math.floor(raiz))) # floor arredonda para baixo"""

"""num = random.random()
print(num)
num1 = random.randint(1,100)
print(num1)"""



"""ns1 = random.randint(1,100)
ns2 = random.randint(1,100)
ns3 = random.randint(1,100)
ns4 = random.randint(1,100)

print("Os numeros sao {} {} {} {}".format (ns1,ns2,ns3,ns4))

print(emoji.emojize("ola, :sunglasses:"))"""




 ############## EXERCICIOS ##################

"""r = float(input("Digite um numero real: "))
print("Sua porção inteira é {}" . format(math.trunc(r)))
print("Sua porção inteira é {}" .format(int(r)))"""


"""co = float(input("Digite o comprimento do cateto oposto "))
ca = float(input("Digite o comprimento do cateto adjacente "))
h2 = math.hypot(co,ca)
print("A Hipotenusa é {:.2f} " . format(h2))"""

"""ang = float(input("Digite o Angulo "))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print("O seno é {:.2f} , o cons é {:.2f} e a tangente é {:.2f}" . format(sen,cos,tan))"""


"""a1 = input("Qual o nome do 1 aluno?")
a2 = input("Qual o nome do 2 aluno?")
a3 = input("Qual o nome do 3 aluno?")
a4 = input("Qual o nome do 4 aluno?")
nomes = [a1,a2,a3,a4]
sort = random.choice(nomes)
print("O aluno escolhido foi {}" . format(sort))"""


"""a1 = input("Qual o nome do 1 aluno?")
a2 = input("Qual o nome do 2 aluno?")
a3 = input("Qual o nome do 3 aluno?")
a4 = input("Qual o nome do 4 aluno?")
nomes = [a1,a2,a3,a4]
random.shuffle(nomes)
print("A ordem é")
print(nomes)"""



""" Quando você chama pygame.init(), ele:
Prepara o mixer de áudio
Configura a janela gráfica
Ativa os módulos de controle de eventos
Verifica se tudo está funcionando"""

"""pygame.init()
pygame.mixer.music.load("nome do arquivo mp3")
pygame.mixer.music.play()
pygame.event.wait()"""



