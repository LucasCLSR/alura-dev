import random
def jogar():


    print("*"*100)
    print("{:*^100}".format(" Seja bem-vindo(a) ao jogo da advinhação. "))
    print("*"*100,"\n")
    print("Tente adivinhar um número aleatório entre 0 e 99.\n")
    total = 0
    i = 0
    pontos = 1000
    while (i == 0):
        print("Selecione um nível de dificuldade.")
        print("(1) Fácil\n(2) Médio\n(3) Difícil")
        total = int(input("> "))
        if(total == 1 or total == 2 or total == 3):
            if(total == 1):
                print("\nVocê escolheu o nível fácil e terá 20 tentativas.")
                total = 20
            elif(total == 2):
                print("\nVocê escolheu o nível médio e terá 10 tentativas.")
                total = 10
            else:
                print("\nVocê escolheu o nível difícil e terá 5 tentativas.")
                total = 5
            i = 1
        else:
            print("\nOpção errada! Escolha entre as 3 opções possíveis.")
    num_secreto = random.randint(0, 99)

    for tentativas in range(1, total + 1):
        print("\nTentativa {} de {}".format(tentativas, total))
        chute = int(input("Digite um número qualquer entre 0 e 99: "))

        if (chute < 0 or chute > 99):
            print("\nPeraí, pô! O número precisa estar entre 0 e 99.")
            continue

        acertou = chute == num_secreto
        maior = chute > num_secreto

        if(acertou):
            print("\nParabéns!!\nVocê acertou após {} tentativas.\nO número secreto realmente é {}.\nSua pontuação foi {}".format(tentativas, num_secreto, pontos))
            break
        elif(maior):
            print("\nSeu chute foi acima do valor. Tente novamente.")
            pontos -= (chute - num_secreto)
        else:
            print("\nSeu chute foi abaixo do valor. Tente novamente.")
            pontos -= (num_secreto - chute)

    if(acertou == False):
        print("\nMesmo após {} tentativas, você não adivinhou o número.".format(total))

    print("\n{:*^100}".format(" Fim do jogo! "))

if(__name__ == "__main__"):
    jogar()
