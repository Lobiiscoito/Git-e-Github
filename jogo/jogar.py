import advinhacao
import forca2
from colorama import init, Fore, Back, Style

# Inicializar a biblioteca colorama
init()


while True:
    print(Fore.YELLOW+"-="*25)
    print("      *********** ", end = '')
    print(Style.RESET_ALL, end='')
    print("ESCOLHA UM JOGO ", end = '' )
    print(Fore.YELLOW+ "***********               ")
    print("-="*25)
    print(Style.RESET_ALL)
    while True:
        print("      (1) Advinhação", end = " / ")
        print("(2) Forca", end = " / ")
        print(Fore.RED+ "(3) SAIR ")
        print(Style.RESET_ALL)
        jogo=int(input(":"))
        if jogo == 1:
            advinhacao.jogar()
        if jogo == 2:
            forca2.jogar2()
        if jogo == 3:
            break
    break


