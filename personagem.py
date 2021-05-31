from opcao import Opcao
from os import system
from inimigo import Inimigo

class Personagem:
    def __init__(self, nome, hp, forca, rodada = 0):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.rodadaAtual = rodada
        self.arma = ""

    def inventario(self, argumento1 = "__", argumento2 = "__",argumento3 = "__"):
        invetario = list()
        invetario.append(argumento1)
        invetario.append(argumento2)
        invetario.append(argumento3)

        print(f'''Inventario: {invetario[0]} | {invetario[1]} | {invetario[2]} 

        ''')

    def Atack(self):
        lv = Inimigo()
        if self.forca > lv.forca:
            print(f"Parabens Você Venceu o Mostro {lv.titulo}\nGanhou +5 Força")
            self.forca += 5
        else:
            print(f"Você Foi Morto Por um Mostro {lv.titulo}")

    def exibeStatus(self): #exibe condicao atual do personagem 
        
        # print(f"{self.hp} - {self.forca} - {self.rodadaAtual}") #print de condicao atual personagem
        system('cls')
        print(f"Jogador: {self.nome}")
        print(f"Vida: {self.hp}")
        print(f"Força: {self.forca}")
        self.inventario(self.arma)
        
    def Dano(self, qtdaDano): #usa os paramentos do mostro 5 = nv1 10 = nv2 15 = boss // considerando seus respectivos danos
        lv = Inimigo()
        lv.Ataque(qtdaDano)
        dano = self.hp - lv.dano
        self.hp = dano

    def armas(self):
        escolhaAtual = Opcao("Machado","Espada","Arco")
        escolhaAtual.escolha()
        selecao = int(input("-> Escolha uma Opção: "))
        if selecao == 1:
            print("Arma Machado Escolhida")
            armae = "Machado"
            self.rodada()
        elif selecao == 2:
            print("Arma Espada Escolhida")
            armae = "Espada"
            self.rodada()
        elif selecao == 3:
            print("Arma Arco Escolhida")
            armae = "Arco"
            self.rodada()
        
        self.arma = armae
        
    def rodada(self):
        self.rodadaAtual += 1
        print(self.rodadaAtual)

       
