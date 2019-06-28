from modulos.turing.maquina import Maquina
from modulos.turing.fita import Fita, Simbolo, Direcao
from modulos.turing.estado import Estado, Transicao

import sys
import re


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

    leitura = leitura.split("000")[1:3]

    transicoes = leitura[0].split("00")
    palavraEntrada = str(leitura[1])

    estadosCriados = {}

    simbolos = {
        "1": Simbolo.a,
        "11": Simbolo.b,
        "111": Simbolo.B
    }

    direcoes = {
        "1": Direcao.DIREITA,
        "11": Direcao.ESQUERDA
    }

    try:
        for transicao in transicoes:
            origem, leitura, destino, escrita, direcao = transicao.split("0")

            if origem not in estadosCriados:
                estadosCriados[origem] = Estado("q{}".format(len(origem)-1))

            if destino not in estadosCriados:
                estadosCriados[destino] = Estado("q{}".format(len(destino)-1))

            estadosCriados[origem].adicionaTransicao(
                leitura=simbolos[leitura], destino=estadosCriados[destino], escrita=simbolos[escrita], direcao=direcoes[direcao])

        maquina = Maquina()

        estadosCriados = list(estadosCriados.values())

        # primeiro estado é inicial
        maquina.adicionaEstado(estadosCriados[0], inicial=True)
        estadosCriados = estadosCriados[1:]

        for estado in estadosCriados:
            maquina.adicionaEstado(estado)

        palavraEntrada = palavraEntrada.replace("111", Simbolo.B.name).replace(
            "11", Simbolo.b.name).replace("1", Simbolo.a.name).split("0")[1:]

        maquina.setEntrada("".join(palavraEntrada))

        i = 1
        while maquina.atuar():
            print("A máquina executou ", i, " vez(es)")
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
