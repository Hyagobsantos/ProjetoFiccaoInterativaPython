from personagem import Personagem
from opcao import Opcao

print('''
 __ ___   _  _    ___ ___ _   _   _ _ _ _  _ __   _  
/ _| __| | |/ \  | o ) __| \_/ | | | | | \| |  \ / \ 
\_ \ _|n_| | o | | o \ _|| \_/ | | V | | \\ | o ) o )
|__/___\__/|_n_| |___/___|_| |_|  \_/|_|_|\_|__/ \_/ 
                                                     
                                                    ''')





#input da classe objeto heroi

nome=str(input('Digite o nome do personagem: '))
heroi = Personagem(nome, 100, 50 ,1)

print("Você está em um quarto e existem armas na sua frente, o que deseja fazer?")
heroi.armas()
#essa parte para baixo não consegui usar a função que você fez 'escolha' como foi usado em heroi.armas()
if heroi.armas ==1:
    print(f'machado está enferrujado')
elif heroi.armas ==2:
    print(f'espada é bem afiada! boa escolha')  
elif heroi.armas == 3:
    print(f'A vantagem do arco e flexa é que você pode atingir o monstro de longe')    
#essa parte de cima não consegui colocar dentro das armas como subnivel
    
print(f'você saiu do quarto... está dentro de um castelo cheio de armadilhas e perigos...cuidado')
print('você está descendo a torre e encontrou um monstro preso em uma jaula....O que deseja fazer?')

obstaculo1=int(input('''   
                        [1]seguir em frente
                        [2]usar sua arma
                        [3]voltar
                    -->   '''))
while True:
    if obstaculo1 == 1:
        print('Boa escolha')    
        break
    elif obstaculo1 == 2:
        print(f'Sua força foi usada')   
        break
    elif obstaculo1 ==3:# aqui era para finalizar o jogo e por + que eu digite 3 continua...
        print(f'você voltou para o quarto e morreu de fome')     
        break 
    
print('você abriu a porta do quarto do rei... tem um monstro te olhando')
obstaculo2=int(input('''O que você faz?
                     [1] sai correndo
                     [2] usa sua arma
                     [3] #não sei oque colocar aqui
                     '''))
if obstaculo2 == 1:
    print('Você se escondeu no quarto ao lado')
if obstaculo2 ==2:
    print('você matou o monstro')    
if obstaculo2 ==3:
    print('')    
    
print('você encontrou uma passagem secreta')

passagem=int(input('''Existem 3 saidas:
                   [1]lado esquerdo
                   [2]lado direito
                   [3]subterraneo
                -->
                   '''))
if passagem ==1:
    print('Você chegou ao calabouço, cheio de grades e cadaveres, precisa voltar')
if passagem ==2:
    print('você conseguiu sair do castelo')    
    print('Você passou de nivel!')
    nivel=int(input('deseja continuar? [S/N]')).upper().strip()[0]
if passagem ==3:
    print('Você caiu no fosso e foi devorado por jacarés') # se ele clivar tem que parar o jogo aqui
