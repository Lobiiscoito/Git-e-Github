from random import randint

def jogar():
    tent= 0
    nivel=0
    
    while True:
        print ('-=-' * 20)
        print ('************ JOGO DA ADIVINHAÇÃO *************')
        print ('-=-' * 20)
        print ('\033[91m[ 1 ]\033[00m DE 0 A 10 / \033[93m[ 2 ]\033[00m DE 0 A 20 / \033[95m[ 3 ]\033[00m DE 0 A 50 / \033[90m[ 4 ]\033[00m DE 0 A 100 / \033[91m[5]\033[00m SAIR')
        print ('-=-'*20)
        nivel = int(input("Escolha uma das Opções \033[91m [1] \033[00m ,\033[93m  [2] \033[00m, \033[95m [3]\033[00m ,\033[90m [4] \033[00m ou \033[91m [5]\033[00m SAIR: " ))
        if nivel == 1:
            computador = randint(0,10)
            print ('-=-' * 20)
            print ( '\033[91m VOU PENSAR EM UM NÚMERO DE 0 A 10 TENTE ADVINHAR\033[00m  ')
            print ('-=-' * 20)
            while True:
                n1= int(input('Qual foi o número q eu pensei? '))
                tent+=1
                if n1 == computador:
                    print (f"!!!!!🎆🎆🎆 PARABENS VOCE CERTOU🎆🎆🎆 !!!!!")
                    print (f"Voce precisou de {tent} tentativas para acertar " )
                    tent = 0
                    computador = randint(0,10)
                    continuar= str(input("Deseja continuar [S] ou [N]: "))
                    if continuar in 'Nn':
                        break
        
                else:
                    if n1 < computador:
                        print('👆👆👆Mais...Tente mais uma vez')
                    elif n1 > computador:
                        print('👇👇👇Menos...Tente mais uma vez')
        if nivel == 2:
            computador = randint(0,20)
            print ('-=-' * 20)
            print ( '\033[93m VOU PENSAR EM UM NÚMERO DE 0 A 20 TENTE ADVINHAR\033[00m ')
            print ('-=-' * 20)
            while True:
                n1= int(input('Qual foi o número q eu pensei? '))
                tent+=1
                if n1 == computador:
                    print (f"!!!!!🎆🎆🎆 PARABENS VOCE CERTOU🎆🎆🎆 !!!!!")
                    print (f"Voce precisou de {tent} tentativas para acertar " )
                    tent = 0
                    computador = randint(0,20)
                    continuar= str(input("Deseja continuar [S] ou [N]: "))
                    if continuar in 'Nn':
                        break
        
                else:
                    if n1 < computador:
                        print('👆👆👆Mais...Tente mais uma vez')
                    elif n1 > computador:
                        print('👇👇👇Menos...Tente mais uma vez')
        if nivel == 3:
            computador = randint(0,50)
            print ('-=-' * 20)
            print ( '\033[95m VOU PENSAR EM UM NÚMERO DE 0 A 50 TENTE ADVINHAR\033[00m ')
            print ('-=-' * 20)
            while True:
                n1= int(input('Qual foi o número q eu pensei? '))
                tent+=1
                if n1 == computador:
                    print (f"!!!!!🎆🎆🎆 PARABENS VOCE CERTOU🎆🎆🎆 !!!!!")
                    print (f"Voce precisou de {tent} tentativas para acertar " )
                    tent = 0
                    computador = randint(0,50)
                    continuar= str(input("Deseja continuar [S] ou [N]: "))
                    if continuar in 'Nn':
                        break
        
                else:
                    if n1 < computador:
                        print('👆👆👆Mais...Tente mais uma vez')
                    elif n1 > computador:
                        print('👇👇👇Menos...Tente mais uma vez')
        
        if nivel == 4:
            computador = randint(0,100)
            print ('-=-' * 20)
            print ( '\033[90m VOU PENSAR EM UM NÚMERO DE 0 A 100 TENTE ADVINHAR\033[00m ')
            print ('-=-' * 20)
            while True:
                n1= int(input('Qual foi o número q eu pensei? '))
                tent+=1
                if n1 == computador:
                    print (f"!!!!!🎆🎆🎆 PARABENS VOCE CERTOU🎆🎆🎆 !!!!!")
                    print (f"Voce precisou de {tent} tentativas para acertar " )
                    tent = 0
                    computador = randint(0,100)
                    continuar= str(input("Deseja continuar [S] ou [N]: "))
                    if continuar in 'Nn':
                        break
        
                else:
                    if n1 < computador:
                        print('👆👆👆Mais...Tente mais uma vez')
                    elif n1 > computador:
                        print('👇👇👇Menos...Tente mais uma vez')
        if nivel == 5:
            break                
if(__name__=="__main__"):
    jogar()
            

    
