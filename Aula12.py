# Estrutura condicional aninhada
nome = str(input("Digite seu nome "))
if nome == "Mayko":
    print("Que nome lindo!")
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print("Seu nome é bem comum.")
elif nome in 'Yudi Okubo':
    print("Que nome maravilhoso")
else:
    print("Seu nome é normal")
print("Tenha um bom dia {}!" .format(nome))