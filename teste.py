import random
par = 0
impar = 0
vitoria = 0
c_par_impar = ''
total = 0

print('\033[;32m ─--─ ─--─ JOGO DO PAR OU ÍMPAR ─--──--─ \033[m')

while True:
   num = int(input('\nEscolha seu número: '))
   par_impar = str(input('Você quer PAR ou ÍMPAR? ')).strip().upper()
   c_num = random.randint(1,10)
   total = num + c_num

   if par_impar == 'PAR' and (num + c_num) % 2 == 0 :
      print('\nVocê \033[32m GANHOU \033[m esta rodada!')
      print(f'Você jogou {num} e o computador jogou {c_num}. O total é {total} e deu PAR')
      vitoria += 1

   if par_impar == 'IMPAR' and (num + c_num) % 2 != 0 :
       print('\nVocê \033[32m GANHOU \033[m esta rodada!')
       vitoria += 1
       print(f'Você jogou {num} e o computador jogou {c_num}. O total é {total} e deu IMPAR')

   else:
       print(f'GAME OVER!! Você venceu {vitoria} vezes')
       print(f'Você jogou {num} e o computador jogou {c_num}.')
       break



