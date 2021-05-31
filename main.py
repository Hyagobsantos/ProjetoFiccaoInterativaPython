import sys
from personagem import Personagem
from opcao import Opcao
from animacaoTexto import animacao 
from os import system
from inimigo import Inimigo
import time

#pensando em criar um menu perguntando se o usuario deseja começar sim ou não // criar tbm no padrao bem vindo 

system('cls') 
texto = (str('''
 __ ___   _  _    ___ ___ _   _   _ _ _ _  _ __   _  
/ _| __| | |/ \  | o ) __| \_/ | | | | | \| |  \ / \ 
\_ \ _|n_| | o | | o \ _|| \_/ | | V | | \\ | o ) o )
|__/___\__/|_n_| |___/___|_| |_|  \_/|_|_|\_|__/ \_/ '''))


animacao(texto)
print("\n")

controle = 1
while controle == 1:
    nome = str(input('Digite o nome do Personagem:\n-> '))
    system('cls')
    heroi = Personagem(nome, 100,10,0)  #instanciando objeto Heroi
    monster = Inimigo()


    texto2 = ("Você está em um quarto e existem armas na sua frente, o que deseja fazer?")
    animacao(texto2)
    
    opcaoEscolha = Opcao("Pegar", "Ignorar")
    opcaoEscolha.escolha()
    selecao = int(input("Escolha uma Opção\n->"))
    if selecao == 1:
        system('cls')
        print("Qual Arma deseja Pegar?")
        heroi.armas()
        heroi.exibeStatus()

    heroi.exibeStatus() 
    texto3 = (''' você saiu do quarto... está dentro de um castelo cheio de armadilhas e perigos...cuidado
                        você está descendo as escadas  da torre Super Rapido...\n''')
    animacao(texto3)
    for i in range(0,18,3):
        espaco = (" "* i) 
        time.sleep(1)
        print(f"{espaco}|__ ")
    print("Alerta Tem Um Mostro A Frente ... O que deseja fazer? ")
    # e encontrou um monstro ....O que deseja fazer?')#preso em uma jaula kkkkkkkk?


    obstaculo = Opcao("Atacar", "Tentar Passar Correndo e Levar Dano", "Fugir")
    obstaculo.escolha()

    obstaculo1=int(input("Escolha uma Opção\n-->"))
    system('cls')
    heroi.exibeStatus()
    while True:
        if obstaculo1 == 1:
            if heroi.arma == "":
                print("Você Não Tem Arma, Escolha Outra Opção:")
                obstaculo = Opcao("Atacar", "Tentar Passar Correndo e Levar Dano", "Fugir")
                obstaculo.escolha()
                obstaculo1=int(input("Escolha uma Opção\n-->"))
            else:
                print("Você Resolveu Atacar O Mostro")
                monster.Ataque(5)
                monster.MostraMostro()
                print(f'Você Esta indo na Direção dele... Rapido {heroi.nome} Use a/o {heroi.arma}')  
                for i in range(0,5):
                    time.sleep(1)
                    print(".")
                heroi.Atack()
                input("Continuar ...")
                break
        elif obstaculo1 == 3:
            print("Você optou por Fugir...")
            print("Você Está Fugindo e Procurando uma sala Vazia Pra se Esconder") 
            for i in range(0,5):
                time.sleep(1)
                print(".")
            print("Parece que Tem uma Aberta ... Rapido Entre:")
            print('''  
                    |--------------------|
                    |                    |
                    |<                   |
                    |--------------------|
                ''')
            print("Aparetemente é uma Sala Segura ....")
            for i in range(0,5):
                time.sleep(1)
                print(".")
            print("Espera que Barulho é Esse ah não!!!")
            for i in range(0,4):
                espaco = (" "* i) 
                time.sleep(1)
                print(f"{espaco}PÀA ")
            print("OH não Eles Entraram Nãoooooo")
            print("Status -> Você Foi Capturado, Torturado e Morto")
            print("GAME OVER") # Gamer Over Pode Ser Animado Acho uma boa 
            again = str(input("Deseja Jogar Novamente ? [S] ou [N]")).strip().upper()[0]
            if again == "S":
                system('cls')
                controle = 1
            else:
                print("Foi um Prazer Te-lo Conosco Volte Sempre!")
                controle = 2
            break
        elif obstaculo1 == 2:
            print(f'você Tentou Passar Correndo Foi Atacado')
            heroi.Dano(5)
            print(f"Você Recebeu Dano do Monstro: {monster.titulo}\n Continuar?")
            input()
            break
        else:
            system('cls')
            obstaculo1=int(input("Opção Invalida Escolha Novamente\n->"))
            obstaculo.escolha()
            
    if obstaculo1 == 1 or obstaculo1 == 2:
        heroi.exibeStatus()    
        print('você abriu a porta do quarto do rei... tem um monstro te olhando')
        print('''              O que você faz?              ''')
        obstaculo = Opcao("Luta Ferosmente", "Tenta Fugir", "Passa Corrente e Toma Dano")
        obstaculo.escolha()
        obstaculo2 = int(input("Escolha Uma Opção"))
        while True:
            if obstaculo2 == 1:
                if heroi.arma == "":
                    print("Você Não Tem Arma, Escolha Outra Opção:")
                    obstaculo = Opcao("Atacar", "Tentar Passar Correndo e Levar Dano", "Fugir")
                    obstaculo.escolha()
                    obstaculo1=int(input("Escolha uma Opção\n->"))
                else:
                    print("Você Resolveu Atacar O Mostro")
                    monster.Ataque(10)
                    monster.MostraMostro()
                    print(f'Você Esta indo na Direção dele... Rapido {heroi.nome} Use a/o {heroi.arma}')  
                    for i in range(0,5):
                        time.sleep(1)
                        print(".")
                    heroi.Atack()
                    break
            elif obstaculo2 == 2:
                print('Você Tentou Fugir Mais Existinham Muitos Mosntros no Caminho Contrario .. e Você Morreu') 
                print("GAMER OVER")
                again = str(input("Deseja Jogar Novamente ? [S] ou [N]")).strip().upper()[0]
                if again == "S":
                    system('cls')
                    controle = 1
                else:
                    print("Foi um Prazer Te-lo Conosco Volte Sempre!")
                    controle = 2
                   
            elif obstaculo2 == 3:
                print(f'você Tentou Passar Correndo Foi Atacado') #precisa incrementar algo aqui ? hein Priscila 
                heroi.Dano(10)
                print(f"Você Recebeu Dano do Monstro: {monster.titulo}\n Continuar?")
                input() 
                break
            else:
                system('cls')
                obstaculo1=int(input("Opção Invalida Escolha Novamente\n->"))
                obstaculo.escolha()
#//////////////////////////////////////////////////////////////// Falta Confronto com o boss e validar o saida 
        system('cls')
        heroi.exibeStatus()
        print('você Derrotou o BOSS e dps da sala dele há uma passagem secreta')
        saida = Opcao("lado esquerdo", "lado direito", "subterraneo")
        saida.escolha()
        saidaFinal = int(input("Escolha Uma Opção\n-->"))
        if saidaFinal ==1:
            print('Você chegou ao calabouço, cheio de grades e cadaveres, precisa voltar')
        elif saidaFinal ==2:
            print('você conseguiu sair do castelo')    
            print('Você passou de nivel!')
            nivel=int(input('deseja continuar? [S/N]')).upper().strip()[0]
        elif saidaFinal ==3:
            print('Você caiu no fosso e foi devorado por jacarés') # se ele clicar tem que parar o jogo aqui
    else:
        again = str(input("Deseja Jogar Novamente ? [S]/[N]")).strip().upper()[0]
        if again == "S":
            system('cls')
            controle = 1
        else:
            print("Foi um Prazer Te-lo Conosco Volte Sempre!")
            controle = 2





    


