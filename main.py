from modulos.turing.maquina import Maquina
from modulos.turing.fita import Fita, Simbolo, Direcao
from modulos.turing.estado import Estado, Transicao

import sys
import re

"""
    Valida os valores passados na entrada do programa. Essa validação segue o padrão de R(M) 
    seguido da palavra de entrada, que será executada pela máquina informada.
"""


def entradaValida(palavra):
    expressao = r"(000)(((1+)(0)(1+)(0)(1+)(0)(1+)(0)(1+)00))*((1+)(0)(1+)(0)(1+)(0)(1+)(0)(1+))(000)(1+)(01+)*(000)"

    return re.match(expressao, palavra)


def main():
    argumentos = sys.argv

    if len(argumentos) != 2:
        print("FALHA: informe o arquivo de entrada, que contenha a R(M) de uma máquina de turing.")
        return

    leitura = open(argumentos[1]).readline()

    if not entradaValida(leitura):
        print("FALHA: A representação recebida não atende o padrão de uma R(M) seguido de entrada.")
        return

    # ignora o primeiro delimitador 000, do inicio da entrada
    leitura = leitura.split("000")[1:3]

    # obtem todas as transições 
    transicoes = leitura[0].split("00")

    #obtem a palavra de entrada
    palavraEntrada = str(leitura[1])

    # cria primeiro todos os estados, lendo suas representações e devidas transições, para posteriormente
    # adicioná-los na máquina
    estadosCriados = {}

    # alfabeto da fita, traduzido do formato unário
    simbolos = {
        "1": Simbolo.a,
        "11": Simbolo.b,
        "111": Simbolo.B
    }

    # direções da fita, traduzido do formato unário
    direcoes = {
        "1": Direcao.DIREITA,
        "11": Direcao.ESQUERDA
    }

    try:
        # converte todas as transições feitas em formato unário numa descrição alto-nível, presente na implementação
        # da máquina de turing atual. Ver arquivo maquina.py
        for transicao in transicoes:
            # obtem todos os parametros da transição
            origem, leitura, destino, escrita, direcao = transicao.split("0")

            # cria os estados (origem e destino) no formato qi, sendo i um indice variado entre [0,Inf[
            if origem not in estadosCriados:
                estadosCriados[origem] = Estado("q{}".format(len(origem)-1))

            if destino not in estadosCriados:
                estadosCriados[destino] = Estado("q{}".format(len(destino)-1))

            # adiciona a transição entre os estados, a partir de seu devido simbolo de leitura, escrita e direção 
            # de movimento na fita
            estadosCriados[origem].adicionaTransicao(
                leitura=simbolos[leitura], destino=estadosCriados[destino], escrita=simbolos[escrita], direcao=direcoes[direcao])

        maquina = Maquina()

        estadosCriados = list(estadosCriados.values())

        # primeiro estado é o inicial
        maquina.adicionaEstado(estadosCriados[0], inicial=True)
        
        estadosCriados = estadosCriados[1:]

        # adiciona todos os estados na máquina de turing
        for estado in estadosCriados:
            maquina.adicionaEstado(estado)

        # decodifica a palavra de entrada, em formato unário, em representação de 
        # alto nível, a partir de um Simbolo (ver arquivo fita.py)
        palavraEntrada = palavraEntrada.replace("111", Simbolo.B.name).replace(
            "11", Simbolo.b.name).replace("1", Simbolo.a.name).split("0")[1:]

        # define a entrada da máquina
        maquina.setEntrada("".join(palavraEntrada))

        i = 1
        # finalmente realiza a execução da máquina de turing informada
        while True:
            if maquina.atuar():
                print("{}a execução da máquina".format(i))
                print()
            else:
                break
            
            i = i + 1
        
    except Exception as identifier:
        print()
        print("Um erro aconteceu durante a execução!")
        print("Detalhes: ")
        print("\t- " + str(identifier))
    finally:
        print()
        print("Fim da execução do simulador.")


main()
