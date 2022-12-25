import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    lista = []
    for palavras in arquivo:
        lista.append(palavras.strip().lower())
    arquivo.close()

    palavra_secreta = random.choice(lista)
    #numero = random.randrange(0, len(lista))
    #palavra_secreta = lista[numero].lower()     (PROFESSOR PEGOU A PALAVRA ALEATOREAMENTE COM randrange, mas do meu jeito tbm funcionou

    letras_acertadas=["_" for letra in palavra_secreta]
    #for item in range(0, len(palavra_secreta)):
     #   letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0
    print("_ "*len(letras_acertadas))
    while(not enforcou and not acertou):
        chute = str(input("Digite uma letra: ")).lower().strip()
        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    #print(f'{chute}, na posição {index}')
                    letras_acertadas[index] = letra
                    print(f'\033[0;32;32mLETRA CORRETA NA POSIÇÃO {index}!\033[m')
                index+= 1
        else:
            erros+= 1
            print(f'\033[0;31;31mVocê errou. {6-erros} tentativas restantes.\033[m')
        print(f'\033[0;31;31m{erros} erros\033[m')
        if erros < 6:
            if letras_acertadas.count('_') == 0:
                print('Você venceu!')
                acertou = True
            else:
                print(f"Ainda faltam {letras_acertadas.count('_')} letras para descobrir!")
                print(f'\n{letras_acertadas}')
        else:
            print('Você perdeu. Fim de jogo.')
            enforcou = True
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
