# Desafio 22
"""n = str(input("Qual o seu nome completo?")).strip()
print(n.upper())
print(n.lower())
print("Ao todo seu nome possui {} letras" .format(len(n)-n.count(' ')))
#   print("O seu primeiro nome tem {} letras" .format(n.find(' '))) # retorna o índice onde a letra/espaço foi encontrada.
separa = n.split()
print("Seu primeiro nome é {} e ele tem {} letras." .format(separa[0], len(separa[0])))"""



# Desafio 23
""" num = int(input("Digite um numero de 0 a 9999: "))
num1 = str(num)

print(" Analisando o numero {}" .format(num1))
print("Unidade: {}" .format(num1[3]))
print("Dezena: {}" .format(num1[2]))
print("Centena: {}" .format(num1[1]))
print("Milhar: {}" .format(num1[0])) """



# Desafio 24
""""cidade = str(input("Digite o nome da uma cidade: ")).strip()
print('Santo' in cidade)
print(cidade[:5].upper() == 'SANTO')"""


# Desafio 25
nome = str(input("Qual o seu nome completo? ")).strip()

n = 'SILVA' in nome
n1 = nome.upper()
print("Seu nome tem Silva no meio? {}" .format(n))



