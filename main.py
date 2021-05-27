from personagem import Personagem


nome = str(input("Digite Seu Nome\n-> "))
genero = str(input("Digite Seu Sexo\n-> ").strip().upper()[0])
idade = int(input("Digite Sua Idade\n-> "))
profissao = int(input('''
            Escolha Sua Profissão:
            [1] - advogado
            [2] - dentista
            [3] - Programador
            ->  '''))
saldo = float(input("Digite um Saldo Maior que 0 Para Começar\n-> "))

if profissao == 1:
    profissao = "Advogado"
elif profissao == 2:
    profissao = "Dentista"
elif profissao == 3:
    profissao = "Programador"

Criacao = Personagem(nome, genero, idade, profissao, saldo)

Criacao.validaSaldo(saldo)

print(Criacao.saldo)

Criacao.mostarObjeto()






 