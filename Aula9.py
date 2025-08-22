""" FATIAMENTO """
frase = "Curso em Video Python"
""" print(frase[9])
print(frase[14:]) # começa do 14 e vai até o final
print(frase[:14]) # começa do começo e vai até o 14
print(frase[9:14]) # Vai de 9 ~ 14
print(frase[9:14:2]) # Vai de 9 ~ 14 pulando de 2 em 2
print(frase[9::2]) # começa no 9 e vai ate o final, pulando de 2 em 2"""

""" Análise """
"""print(len(frase)) # mostra a quantitade de caracteres
print(frase.count('o')) # CONTA quantas vezes aparece a leta 'o'
print(frase.count('o',0,14)) # CONTA os '0' da posição 0 ~ 14
print(frase.find('deo')) # Mostra em que posição a frase 'deo' começou
print(frase.find('Android')) # vai mostrar -1, significa que nao foi encontrado
print('Curso' in frase) # Pergunta se existe 'curso' na variavel  frase"""


""" TRANSFORMAÇÃO"""
"""print(frase.replace('Python','JavaScript')) # substitui a palavra, mas nao na frase original
print(frase.upper()) # Coloca as letras minusculas em Maiusculas
print(frase.lower()) # Coloca as letras maiusculas em minusculas
print(frase.capitalize()) # coloca a primeira letra em maiusculo e o resto em minusculo
print(frase.title()) # Ele coloca a primeira letra de toda palavra em maiusculo
print(frase.strip()) # Remove os espaço inuteis do começo e do fim.
print(frase.lstrip()) # remove espaço da esquerda
print(frase.rstrip()) # remove espaço da direita"""


"""Divisão"""
print(frase.split()) # ocorre uma divisão considerando os espaços, gera uma lista.
print('-'.join(frase)) # Coloca um caractere em todo espaço dentre os caracteres
print(frase.replace(' ', '-')) # hifen nos lugares dos espaços
