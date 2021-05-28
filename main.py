from personagem import Personagem
from animacaoTexto import animacao


# nome = str(input("Digite Seu Nome\n-> "))
# genero = str(input("Digite Seu Sexo\n-> ").strip().upper()[0])
# idade = int(input("Digite Sua Idade\n-> "))
# profissao = int(input('''
#             Escolha Sua Profissão:
#             [1] - advogado
#             [2] - dentista
#             [3] - Programador
#             ->  '''))
# saldo = float(input("Digite um Saldo Maior que 0 Para Começar\n-> "))

# if profissao == 1:
#     profissao = "Advogado"
# elif profissao == 2:
#     profissao = "Dentista"
# elif profissao == 3:
#     profissao = "Programador"

# Criacao = Personagem(nome, genero, idade, profissao, saldo)

# Criacao.validaSaldo(saldo)

# print(Criacao.saldo)

# Criacao.mostarObjeto()


comida = Personagem() #!--Classe instanciada ALimentação Validada Pronto Para Usar --!
#validar as opçoes

# textoAlimentacao  = ('''
#         escolha as seguites opções de alimentos para matar sua fome:
#             [1]-chocolate
#             [2]-hamburger
#             [3]-pizza
#             [4]-fruta
#             [5]-comida caseira\n->''')
# animacao(textoAlimentacao)
periodo = str(input("Digite um Periodo:"))
escolha = int(input("Digite uma opçao"))


comida.alimentar(periodo, escolha)








 