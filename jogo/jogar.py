import advinhacao
import forca2

print("-="*30)
print("********* ESCOLHA UM JOGO *********")
print("-="*30)
jogo=int(input("(1) Advinhação (2) Forca    (3) : "))

if jogo == 1:
    print("Jogando Advinhação")
    advinhacao.jogar()
if jogo == 2:
    print("Jogando forca")
    forca2.jogar2()

print("-="*30)
print("********* ESCOLHA UM JOGO *********")
print("-="*30)
jogo=int(input("(1) Advinhação (2) Forca    (3) : "))