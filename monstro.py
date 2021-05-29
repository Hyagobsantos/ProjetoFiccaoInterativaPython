class Monstro:
    def __init__(self, força, defesa):
        self.força = força
        self.defesa = defesa
    
    def Ataque(self, ataque=50):
        self.força.Ataque(50) -= #defesa do personagem
        print(f'seu personagem foi atacado e perdeu {} ')

    def Esquiva(self. esquiva=30):
        self.defesa.Esquiva(30) -= #ataque do personagem
        print(f'O monsto desviu do seu ataque {}')
