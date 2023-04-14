import random

def jogar2():
    boas_vindas()
    while True:
        palavra_secreta = carregar_palavra_secreta()
        letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
        print(letras_acertadas)
        

        enforcou = False
        acertou = False
        erros = 0


        while(not enforcou and not acertou):
            print()
            chute = solicitacao_do_chute()

            if(chute in palavra_secreta):
                corrigindo_chute(chute, palavra_secreta, letras_acertadas)
            else:
                erros += 1
                desenha_forca(erros)

            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)


        if(acertou):
            mensagem_vencedor()
        else:
            mensagem_perdedor(palavra_secreta)
        print()
        print("Fim do jogo")
       
       # opção se quer continuar
       
        while True:
            continuar= str(input("Deseja continuar [S] ou [N]: ")).upper()
            if continuar in 'SN':
                    break
        if continuar in 'Nn':
            break
        
def boas_vindas():
        print("*************************************")
        print("**** Bem vindo ao jogo da Forca! ****")
        print("*************************************")

def carregar_palavra_secreta():
    with open(r'C:\Users\lobii\OneDrive\Área de Trabalho\VS code\Python\Jogos\palavras.txt',) as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))

        print()
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def solicitacao_do_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def corrigindo_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
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
        print(" |            ")

    if(erros == 6):
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


def mensagem_vencedor():
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

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
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


if(__name__ == "__main__"):
    jogar2()