import time, sys

def animacao(texto):
    frase = texto

    for i in list(frase):
        print(i, end='')
        #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
        #@josucka vc ta falando de qual parte aqui nesse comentario... eu meio que nao entendi pq vc ja fez esse import
        sys.stdout.flush()
        time.sleep(0.099)
 