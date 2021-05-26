class Personagem:
    def __init__(self, nome = '',sexo = '', idade = 0, ocupacao = 0, saldoBancario = 0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.ocupacao = ocupacao
        self.saldo = saldoBancario
    

    def validaSaldo(self, valorAtual):
        while True:
            valorAtual = float(input("Digite um saldo maior que 0"))
            if valorAtual > 0: #while seria um boa aqui 
                self.saldo = valorAtual
                break
                
            
                  
            

    def mostarObjeto(self):
        print(f"\nNome: {self.nome}\nGenero: {self.sexo}\nIdade: {self.idade}\nOcupação: {self.ocupacao}\nSaldo: {self.saldo}")



