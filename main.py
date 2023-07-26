import random

pontuacao = 200
numero_tentativa = 0
dificuldade = -1

print("Venha jogar!")

while (dificuldade < 1 or dificuldade > 3):
  dificuldade = int(input("Escolha a dificuldade: (1)Fácil (2)Médio (3)Difícil\n"))
  if (dificuldade < 1 or dificuldade > 3):
    print("Escolha um valor adequado!")

if (dificuldade == 1):
  numero_tentativa = 15
  penalidade = 13
elif (dificuldade == 2):
  numero_tentativa = 10
  penalidade = 19
elif (dificuldade == 3):
  numero_tentativa = 5
  penalidade = 35
gabarito = random.randrange(1, 101)
chute = 0

for rodada in range(1, numero_tentativa + 1):
  print("Rodada {} de {}".format(rodada, numero_tentativa))
  chute = int(input("Chute um número de 1 a 100\n"))
  if (chute == gabarito):
    print("Parabens você acertou\n")
    pontuacao -= (rodada-1) * penalidade
    print("Sua pontuacao foi {} parabens\n".format(pontuacao))
    print ("Fim do jogo. Obrigado por jogar!\n")
    exit(0)
  if (chute > 101 or chute < 1):
    print("O número deve ser entre 1 e 100, você digitou {}\n".format(chute))
    continue
  if(chute > gabarito):
      print("Você errou. O número é menor do que isso...\n")
  elif(chute < gabarito):
      print("você errou. O número é maior do que isso...\n")

print ("Você perdeu, o número era {} Fim do jogo. Obrigado por jogar!\n".format(gabarito))
