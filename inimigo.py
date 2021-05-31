class Inimigo:
    def __init__(self, força = 0, defesa = 0, titulo = ""):
        self.forca = força
        self.dano = defesa
        self.titulo = titulo
    
    def Ataque(self, tamanho):
        self.tamanho = tamanho
        if self.tamanho == 5:
            self.titulo = "LV 1"
            self.forca = 5
            self.dano = 3
        elif self.tamanho == 10:
            self.titulo = "LV 2"
            self.forca = 10
            self.dano = 6
        elif self.tamanho == 15:
            self.titulo = "BOSS"
            self.forca = 15
            self.dano = 9

    def MostraMostro(self):
        print(f"Status do Monstro: {self.titulo} | Força: {self.forca} | Dano: {self.dano}")