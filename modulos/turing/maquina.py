from enum import Enum

from modulos.turing.fita import Simbolo, Direcao, Fita
from modulos.turing.estado import Estado, Transicao


class Maquina:
    def __init__(self):
        self.heuristica = []
        self.fita = Fita()
        self.estadoInicial = None
        self.estadoAtual = None

        self.estados = []

    """
        Adiciona um novo estado na representação da máquina de Turing.

        Parametros: 
            1) estado: simbologia de estado, instância da classe Estado
            2) inicial: flag que indica se estado é ou não inicial
    """

    def adicionaEstado(self, estado, inicial=False):
        if not isinstance(estado, Estado):
            raise Exception(
                "[Maquina::adicionaEstado]: Os estados de uma máquina de turing precisam ser instâncias de Estado.")

        self.estados.append(estado)

        if inicial:
            self.estadoAtual = estado
        self.heuristica.append([])


    def atuar(self):
        print(self.fita)
        
        simboloAtual = self.fita.ler()
        transicao = self.estadoAtual.obterTransicao(simboloAtual)
        realizado = False
        if (transicao is not None):
            self.estadoAtual = transicao.destino

            self.fita.escrever(transicao.escrita)
            self.fita.mover(transicao.direcao)
            realizado = True
        loop = self.verificaLoop()
        if loop and realizado:
            raise Exception("Loop BIG HEAD DE CAGANEIRA")
        return realizado

    def setEntrada(self, entrada):
        # pula o primeiro branco
        self.fita.mover(Direcao.DIREITA)

        for simbolo in entrada:
            if simbolo == 'a':
                self.fita.escrever(Simbolo.a)
            elif simbolo == 'b':
                self.fita.escrever(Simbolo.b)
            else:
                self.fita.escrever(Simbolo.B)

            self.fita.mover(Direcao.DIREITA)

        while(self.fita.posicao != 0):
            self.fita.mover(Direcao.ESQUERDA)

    def verificaLoop(self):
        loop = False
        localEstado = 0
        for estado in self.estados:
            if estado != self.estadoAtual:
                localEstado += 1
            else:
                break
        if ({self.fita.getPosicao():self.fita.getConteudo()}) in self.heuristica[localEstado]:
            return True
        else:
            self.heuristica[localEstado].append({self.fita.getPosicao():self.fita.getConteudo()})
            return False


