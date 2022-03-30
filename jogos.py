import jogo_da_advinhacao
import jogo_da_forca

def escolhe_jogo():
    print("~"*100)
    print("{:~^100}".format(" Escolha o seu jogo "))
    print("~"*100,"\n")

    print("(1) Jogo da Forca\n(2) Jogo da adivinhação")
    jogo = int(input("> "))
    i = 0
    while(i == 0):
        if(jogo == 1):
            print("Abrindo jogo da forca...\n\n")
            jogo_da_forca.jogar()
            i = 1
        elif(jogo == 2):
            print("Abrindo jogo da adivinhação...\n\n")
            jogo_da_advinhacao.jogar()
            i = 1
        else:
            print("Escolha uma opção válida.\n")

if(__name__ == "__main__"):
    escolhe_jogo()
