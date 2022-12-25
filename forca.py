import random


def mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def abrir_arquivo_e_define_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        lista = []
        for palavras in arquivo:
            lista.append(palavras.strip().lower())
    palavra_secreta = random.choice(lista)
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas


def pede_chute():
    chute = str(input("Digite uma letra: ")).lower().strip()
    return chute


def alimenta_com_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            # print(f'{chute}, na posição {index}')
            letras_acertadas[index] = letra
            print(f'\033[0;32;32mLETRA CORRETA NA POSIÇÃO {index}!\033[m')
        index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    mensagem_de_abertura()
    palavra_secreta = abrir_arquivo_e_define_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0
    print("_ " * len(letras_acertadas))
    while (not enforcou and not acertou):
        chute = pede_chute()
        if chute in palavra_secreta:
            alimenta_com_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print(f'\033[0;31;31mVocê errou. {7 - erros} tentativas restantes.\033[m')
        #print(f'\033[0;31;31m{erros} erros\033[m')
        if erros < 7:
            if letras_acertadas.count('_') == 0:
                print('Você venceu!')
                print(imprime_mensagem_vencedor())
                acertou = True
            else:
                print(f"Ainda faltam {letras_acertadas.count('_')} letras para descobrir!")
                print(f'\n{letras_acertadas}')
        else:
            print('Você perdeu. Fim de jogo.')
            print(imprime_mensagem_perdedor(palavra_secreta))
            enforcou = True
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
