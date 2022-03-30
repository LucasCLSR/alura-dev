import random

def imprime_abertura():
    print("*"*100)
    print("{:*^100}".format(" Seja bem-vindo(a) ao jogo da Forca. "))
    print("*"*100,"\n")

def escolhe_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo: # with dispensa a necessidade de fechar o arquivo
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Informe uma letra: ")
    return chute.strip().upper()

def chute_certo(palavra_secreta, chute, letras_acertadas):
    i = 0
    for letra in palavra_secreta:
        if(letra == chute):
            letras_acertadas[i] = letra
        i += 1

def imprime_encerramento():
    print("\n{:*^100}".format(" Fim do jogo! "))

def jogar():
    
    imprime_abertura()
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    print("Palavra secreta: ", "_ "*len(letras_acertadas))

    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            chute_certo(palavra_secreta, chute, letras_acertadas)
            
            print("\nPalavra secreta: ", letras_acertadas)
        else:
            erros += 1
            if(erros == 6):
                print("\nEssa letra não consta na palavra secreta. Suas chances acabaram.")
                imprime_forca(erros)
            else:
                print("\nEssa letra não consta na palavra secreta. Você ainda tem {} chances.".format(6 - erros))
                imprime_forca(erros)
            print("\nPalavra secreta: ", letras_acertadas)
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    
    if(acertou):
        print("\nParabéns, você acertou! A palavra certa é {}".format(palavra_secreta))
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    imprime_encerramento()

def imprime_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado! Não foi dessa vez.")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________       ")
    print("    /               \      ")
    print("   /                 \     ")
    print(" //                   \/\  ")
    print(" \|   XXXX     XXXX   | /  ")
    print("  |   XXXX     XXXX   |/   ")
    print("  |   XXX       XXX   |    ")
    print("  |                   |    ")
    print("  \__      XXX      __/    ")
    print("    |\     XXX     /|      ")
    print("    | |           | |      ")
    print("    | I I I I I I I |      ")
    print("    |  I I I I I I  |      ")
    print("    \_             _/      ")
    print("      \_         _/        ")
    print("        \_______/          ")

if(__name__ == "__main__"):
    jogar()