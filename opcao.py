class Opcaoes:
    def __init__(self, opcao):
        self.opcao = opcao
#opcao generica capitulo 0
    def escolha(self, escolha1, escolha2, escolha3):
        if escolha1 != "":
            print("1-", escolha1)
        elif escolha2 != "":
            print("2-", escolha2)
        elif escolha3 != "":
            print("3-", escolha3)
        
