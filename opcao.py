#opcao generica capitulo 0
class Opcao:
    def __init__(self,escolha1, escolha2,escolha3 = ""):
        self.escolha1 = escolha1
        self.escolha2 = escolha2
        self.escolha3 = escolha3

    def escolha(self): #exibe apenas as opçoes // validaçoes posteriores seram realizadas no main

        if self.escolha3 == "":
            print(f'''
            [1] - {self.escolha1}
            [2] - {self.escolha2}
            ''')
        else:
            print(f'''
            [1] - {self.escolha1}
            [2] - {self.escolha2}
            [3] - {self.escolha3}
            ''')








    