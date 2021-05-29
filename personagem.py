from opcao import Opcaoes

class Personagem:
    def __init__(self, nome, hp, forca, rodada):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.rodadaAtual = rodada

    def exibecondicaoatual(self): #exibe condicao atual do personagem 
        print(f"{self.hp} - {self.forca} - {self.rodadaAtual}") #print de condicao atual personagem
    

    def armas(self):
        escolhaAtual = Opcaoes("Machado","Espada","Arco")
        escolhaAtual.escolha()
        selecao = int(input())
        if selecao == 1:
            print("Arma Machado Escolhida")
        elif selecao == 2:
            print("Arma Espada Escolhida")
        elif selecao == 3:
            print("Arma Arco Escolhida")

    def rodada(self):
        self.rodadaAtual += 1

       
