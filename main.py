import sys
from personagem import Personagem
from opcao import Opcao
from animacaoTexto import animacao 
from os import system
from inimigo import Inimigo
import time

system('cls') 

#talvez seja melhor tirar o seja e deixar só o bem vindo, talvez com outra fonte, o que acha? ai em baixo do bem vindo coloca as opções do menu
texto = str('''
                            __ ___   _  _    ___ ___ _   _   _ _ _ _  _ __   _  
                            / _| __| | |/ \  | o ) __| \_/ | | | | | \| |  \ / \ 
                            \_ \ _|n_| | o | | o \ _|| \_/ | | V | | \\ | o ) o )
                            |__/___\__/|_n_| |___/___|_| |_|  \_/|_|_|\_|__/ \_/ ''')

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
    print('''
                                                      _,--~~~,
                                                    .'        `.
                                                    |           ;
                                                    |           :
                                                   /_,-==/     .'
                                                 /'`\*  ;      :      
                                               :'    `-        :      
                                               `~*,'     .     :      
                                                  :__.,._  `;  :      
                                                  `/'    )  '  `,     
                                                      \-/  '     )     
                                                      :'          \ _
                                                       `~---,-~    `,)
                                       ___                   \     /~`/
                                 \---__ `;~~~-------------~~~(| _-'    `,
                               ---, ' \`-._____     _______.---'        
                              \--- `~~-`,      ~~~~~~                     
                             \----      )                                  
                             \----.  __ /                                    
                              \----'` -~____  
                                            ~~~~~--------,.___     
                                                              ```\_
                                       ''')


    obstaculo = Opcao("Atacar", "Fugir", "Tentar Passar Correndo e Levar Dano")
    obstaculo.escolha()

    obstaculo1=int(input("Escolha uma Opção\n-->"))
    system('cls')
    heroi.exibeStatus()
    
    while True:
        if obstaculo1 == 1:
            if heroi.arma == "":
                print("Você Não Tem Arma, Escolha Outra Opção:")
                obstaculo = Opcao("Atacar", "Fugir", "Tentar Passar Correndo e Levar Dano")
                obstaculo.escolha()
                obstaculo1=int(input("Escolha uma Opção\n-->"))

            else:
                print("Você Resolveu Atacar o Monstro")
                monster.Ataque(5)
                monster.MostraMostro()
                print(f'Você Esta indo na Direção dele... Rapido {heroi.nome} Use a/o {heroi.arma}')  
                for i in range(0,3):
                    time.sleep(1)
                    print(".")
                heroi.Atack()
                input("Digite SIM para continuar ...")
                break
                
        elif obstaculo1 == 2:
            print("Você optou por Fugir...")
            print("Você Está Fugindo e Procurando uma sala Vazia Pra se Esconder") 
            for i in range(0,3):
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
            for i in range(0,3):
                time.sleep(1)
                print(".")
            print("Espera que Barulho é Esse ah não!!!")
            for i in range(0,2):
                espaco = (" "* i) 
                time.sleep(1)
                print(f"{espaco}PÀA ")
            print("OH não Eles Entraram Nãoooooo")
            print('''                                      
                                 _ _                        /               \           
                             -/~/ / ~\                     :;                \       ___¨¨¨¨¨__
                            || | | /\ ;\                   |l      _____     |;     ( \/    > >
                            _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \      //
                           ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
                          (((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
                          )))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
                          ((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
                           )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
                           |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
                           |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
                           ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
                             ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
                                ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
                           :       ;                     `.      "``::::::''    .'
                              ;                           `.   \_              /
                            ;       ;                       +:   ~~--  `:'  -';
                                                             `:         : .::/  -
                                ;                            ;;+_  :::. :..;;;  
                                                             ;;;;;;,;;;;;;;;,;
                  ''') 
            print("Status -> Você Foi Capturado, Torturado e Morto")
            texto5 = ("""  
                     
                                      (  ____ \(  ___  )(       )(  ____ \   (  ___  )|\     /|(  ____ \(  ____ )
                                      | (    \/| (   ) || () () || (    \/   | (   ) || )   ( || (    \/| (    )|
                                      | |      | (___) || || || || (__       | |   | || |   | || (__    | (____)|
                                      | | ____ |  ___  || |(_)| ||  __)      | |   | |( (   ) )|  __)   |     __)
                                      | | \_  )| (   ) || |   | || (         | |   | | \ \_/ / | (      | (\ (   
                                      | (___) || )   ( || )   ( || (____/\   | (___) |  \   /  | (____/\| ) \ \__
                                      (_______)|/     \||/     \|(_______/   (_______)   \_/   (_______/|/   \__/       
                    """)
            animacao(texto5)
            print("\n")
            again = str(input("Deseja Jogar Novamente ? [S] ou [N]").strip().upper()[0])
            if again == "S":
                system('cls')
                controle = 1
                break
            else:
                print("Foi um Prazer Te-lo Conosco Volte Sempre!")
                controle = 2
                break
            
        elif obstaculo1 == 3:
            print(f'você Tentou Passar Correndo Foi Atacado')
            heroi.Dano(5)
            print(f"Você Recebeu Dano do Monstro: {monster.titulo}\n Continuar?")
            input()
            break
        
        else:
            system('cls')
            obstaculo = Opcao("Atacar", "Fugir", "Tentar Passar Correndo e Levar Dano")
            obstaculo.escolha()
            obstaculo1= int(input("Opção Invalida Escolha Novamente\n->"))

    
    heroi.exibeStatus()  
    system('cls')  
    print('você abriu a porta do quarto do rei... tem um monstro te olhando')
    print('''              
                                                            (    )
                                                            ((((()))
                                                            |o\ /o)|
                                                            ( (  _')
                                                            (._.  /\__
                                                            ,\___,/ '  ')
                                            '.,_,,       (  .- .   .    )
                                            \   \\     ( '        )(    )
                                                \   \\    \.  _.__ ____( .  |
                                                \  /\\   .(   .'  /\  '.  )
                                                \(  \\.-' ( /    \/    \)
                                                '  ()) _'.-|/\/\/\/\/\|
                                                    '\\ .( |\/\/\/\/\/|
                                                        '((  \    /\    /
                                                        ((((  '.__\/__.')
                                                        ((,) /   ((()   )
                                                        "..-,  (()("   /
                                                            _//.   ((() ."
                                                    _____ //,/" ___ ((( ', ___
                                                                    ((  )
                                                                    / /
                                                                    _/,/'
                                                                /,/,"
    ''')
    print("\n")
    print('''              O que você faz?              ''')
    obstaculo = Opcao("Luta Ferosmente", "Tenta Fugir", "Passa Corrente e Toma Dano")
    obstaculo.escolha()
    obstaculo2 = int(input("Escolha Uma Opção\n-->"))
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
            print('Você Tentou Fugir Mais Existinham Muitos Monstros no Caminho Contrario .. e Você Morreu') 
            print("""  
                    
                                    (  ____ \(  ___  )(       )(  ____ \   (  ___  )|\     /|(  ____ \(  ____ )
                                    | (    \/| (   ) || () () || (    \/   | (   ) || )   ( || (    \/| (    )|
                                    | |      | (___) || || || || (__       | |   | || |   | || (__    | (____)|
                                    | | ____ |  ___  || |(_)| ||  __)      | |   | |( (   ) )|  __)   |     __)
                                    | | \_  )| (   ) || |   | || (         | |   | | \ \_/ / | (      | (\ (   
                                    | (___) || )   ( || )   ( || (____/\   | (___) |  \   /  | (____/\| ) \ \__
                                    (_______)|/     \||/     \|(_______/   (_______)   \_/   (_______/|/   \__/       
                """)#quando clico no N ele mostra foi um prazer te-lo conosto e o game over aparece embaixo denovo
            again = str(input("Deseja Jogar Novamente ? [S] ou [N]")).strip().upper()[0]#quando clico no S ele não está fazendo nada, só obecede no N
            if again == "S":
                system('cls')
                controle = 1
                break
            else:
                print("Foi um Prazer Te-lo Conosco Volte Sempre!")
                controle = 2
                break
                
        elif obstaculo2 == 3:
            print(f'você Tentou Passar Correndo Foi Atacado') #precisa incrementar algo aqui ? hein Priscila 
            #pode ser um "O monstro foi mais rápido e te atacou primeiro"
            heroi.Dano(10)
            print(f"Você Recebeu Dano do Monstro: {monster.titulo}\n Continuar?")
            input() 
            break
        else:
            system('cls')
            obstaculo1=int(input("Opção Invalida Escolha Novamente\n->"))
            obstaculo.escolha()
    system('cls')
    heroi.exibeStatus()
    print("Você está indo muito bem Continue Assim")
    for i in range(0,5):
        time.sleep(1)
        print(".")
    print('Agora Você chegou no salão principal do castelo Cuidado com esse monstro poderoso ... Reaja ele está aí vindo na sua direção... ')
    print('''              
                                                              BOSS
                                                        __________________                                     
                                                    __/______/    \______\__                                  
                                                    (________( <[]> )________)                                 
                                                    \________\    /________/                                  
                                                      /\________\__/________/\             
                                                    (((\  .___      ___,  /)))         
                                                      ||||  (<@)      (@>)  ||||            
                                                     )))\       (__,     /(((           
                                                     (((  )  __________ (  )))        
                                                       )))(  \VvVvVvVv/  )(((         
                                                      (((  \ (AAAAAAAA) /  )))         
                                                            \__________/                    
                                                                |  |
                                                         _\_____)<>(_____/_                      
                                                         /    /    \    \                                      
                                                             (_.--._)                   
                                                             ((    ))                   
                                                              _))  ((_  
        ''')
    print('Seja rápido e descubra o ponto fraco do BOSS')
    batalha = Opcao("barriga","Pescoço","Olhos")
    batalha.escolha()
    batalha1 = int(input("Escolha uma Opção\n--> "))
    while True:
        if batalha1 == 1:
            print('Você machucou o Boss e deixou ele muito irritado, ataque outro ponto fraco!')
            batalha = Opcao("barriga","Pescoço","Olhos")
            batalha.escolha()
            batalha1 = int(input("Escolha uma Opção Diferente \n--> "))
        elif batalha1 == 2:
            monster.Ataque(15)
            print(f'Você acertou o ponto fraco e deu um golpe fatal no {monster.titulo}') 
            print(f'Você Esta indo na Direção dele... Rapido {heroi.nome} Mate-o')  
            for i in range(0,5):
                time.sleep(1)
                print(".")
            heroi.Atack()
            break
        elif batalha1 == 3:
            print('Você deixou o BOSS cego, ataque novamente')
            batalha = Opcao("barriga","Pescoço","Olhos")
            batalha.escolha()
            batalha1 = int(input("Escolha uma Opção Difetente\n--> "))       
    #aqui quando clica na opção 1 e 3 (quando não mata o monstro) pula o jogo reinicia
    system('cls')
    heroi.exibeStatus()
    print('você Derrotou o BOSS a porta principal está trancada! você encostou na parede e encontrou  uma passagem secreta, você entrou e encontrou 3 saídas, qual você escolhe?')
    saida = Opcao("lado esquerdo", "lado direito", "subterraneo")
    saida.escolha()
    saidaFinal = int(input("Escolha Uma Opção\n-->"))
    if saidaFinal == 1:
        print('Você chegou ao calabouço, cheio de grades e cadaveres, precisa voltar') #valido // pode se perdeu e morreu
    elif saidaFinal ==2:
        print('você conseguiu sair do castelo')    
        print('Você Finalizou O Jogo')
        nivel=int(input('deseja continuar? [S/N]').upper().strip()[0])
        if again == "S":
            system('cls')
            controle = 1
        else:
            print("Foi um Prazer Te-lo Conosco Volte Sempre!")
            controle = 2
    elif saidaFinal ==3:
        print('Você caiu no fosso e foi devorado por jacarés') # se ele clicar tem que parar o jogo aqui e continua
    
    again = str(input("Deseja Jogar Novamente ? [S]/[N]").strip().upper()[0])
    if again == "S":
        system('cls')
        controle = 1
    else:
        print("Foi um Prazer Te-lo Conosco Volte Sempre!")
        controle = 2

