class Personagem:
    def __init__(self, nome = '',sexo = '', idade = 0, ocupacao = 0, saldoBancario = 0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.ocupacao = ocupacao
        self.saldo = saldoBancario
    

    def validaSaldo(self, valorAtual):
        while True:
            valorAtual = float(input("Você Digitou o Valor 0, Digite Novamente:"))
            if valorAtual > 0: 
                self.saldo = valorAtual
                break
                
    def localAtual(self, camihada):
        local = camihada
        print(f"Local Atual: {local}")


    def alimentar(self, comida):
            
            if comida == 1:
                print('Hummm! Você comeu chocolate') 
            elif comida == 2:
                print('o hamburger estava uma delícia') 
            elif comida == 3: 
                escolha = ""
                quantidade = 0
                restante = 8
                escolha = str(input("Escolha o Sabor da Pizza: "))
                print(f"Você Escolheu o Sabor {escolha} é Comeu um Pedaço")
                while True:
                    quantidade = str(input('deseja comer mais um pedaço [S] - [N]').strip().upper()[0])
                    if quantidade in 'S':
                        restante -= 1
                        print(f"Parece que está muito bom vc comeu +1 Pedaço e tem mais {restante}")
                        if restante == 0:
                            print("Você Já Comeu todos os 8 Pegaços")
                            break
                    else:
                        break
           
            
    def mostarObjeto(self):
        print(f"\nNome: {self.nome}\nGenero: {self.sexo}\nIdade: {self.idade}\nOcupação: {self.ocupacao}\nSaldo: {self.saldo}")



