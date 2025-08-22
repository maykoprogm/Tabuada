resultado = 0

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


print('Programa finalizado.')