import json

def mostrar_receita(drink):
    with open ('receitas.json', 'r', encoding='utf-8') as f:
        receitas = json.load(f)

        drink = drink.lower()
        if drink in receitas:
            receita = receitas[drink]

            print("Receita do(a) {}:" .format(drink.capitalize()))
            print("Ingredientes: ")
            for item in receita['ingredientes']:
                print("- " + item)

            print("\nModo de preparo")
            for item in receita['modo_preparo']:
                print('- ' + item)

        else:
            print("Bebida não encontrada.")




while True:
 n = str(input("\n ** Qual drink você quer saber a receita? ** \n( ou digite 'sair' para encerrar.)\n"))
 mostrar_receita(n)
 if ( n.lower() ==  'sair'):
     print("Encerrando o programa...")
     break

