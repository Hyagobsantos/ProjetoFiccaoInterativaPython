from opcao import Opcaoes

class Personagem:
    def __init__(self, nome, hp, forca):
        self.nome = nome
        self.hp = hp
        self.forca = forca

    def exibecondicaoatual(self): #exibe condicao atual do personagem 
        print(f"{self.hp} - {self.forca}") #print de condicao atual personagem
    

    def armas(self, arma):
        escolhaAtual = Opcaoes()
        escolhaAtual.escolha("Machado","Espada","Arco")
       




#3 
# armas 1 = equlibrio -> hp: 10 forca: 10 
#arma 2 = vida -> hp: 18 forca: 2
#arma 3 = forca -> hp: 2 forca: 18