#inteiros = [1,3,4,5,7,8,9]
#pares = []
#for numero in inteiros:
#    if numero % 2 == 0:
#        pares.append(numero)
#print(pares)


#pares2 = [numero for numero in inteiros if numero % 2 == 0]
#print(pares2)

#palavras = open("palavras.txt", "w")
#palavras.write("melão\nmaça\ncaqui\ntangerina\nabacaxi")
#palavras.close()
#print(palavras)

import random
# FUNÇÕES

def imprime_msg_abertura():
    print('-=-' * 20)
    print('#' * 7, "Bem vindo ao jogo da Forca!", '#' * 7)
    print('-=-' * 20)


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    print("A palavra tem {} letras".format(len(palavra_secreta)))

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("DIGITE UMA LETRA: ")  # ENTRADA LETRA
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, palavras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            palavras_acertadas[index] = letra
        index = index + 1


def msg_vencedor():
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


def msg_perdedor(palavra_secreta):
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


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()

    palavras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(palavras_acertadas)


    #acertou = False

    tentativas = 7
    erros = 0
    print(f"Você tem {tentativas} tentativas para encontrar a palavra")
    #while (not acertou and not enforcou):
    while (tentativas > 0):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, palavras_acertadas)

        else:
            print(f"Letra não existe na palavra, você ainda possui {tentativas - 1} tentativas")
            tentativas -= 1
            erros += 1
            desenha_forca(erros)

        print(palavras_acertadas)

    if ("_" not in palavras_acertadas):
        msg_vencedor()
    elif(tentativas == 0):
        msg_perdedor(palavra_secreta)





if (__name__ == "__main__"):
    jogar()