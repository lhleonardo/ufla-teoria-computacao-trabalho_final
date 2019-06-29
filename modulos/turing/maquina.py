from enum import Enum

from modulos.turing.fita import Simbolo, Direcao, Fita
from modulos.turing.estado import Estado, Transicao


class Maquina:
    def __init__(self):
        self.fita = Fita()
        self.estadoInicial = None
        self.estadoAtual = None

        self.estados = []

        # definição de um histórico de passadas via transições
        # utilizado para aplicação da heurística que resolve o problema da parada
        self.historico = []

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

        # cria-se uma posição para cada estado adicionado na máquina
        self.historico.append([])

    """
        Executa uma operação em cima da máquina e seus posicionamentos atuais. 

        Cada atuação lê o estado atual, simbolo presente na fita e executa uma transição específica.

        Máquina não comprovada para não determinismo. Não se sabe seu comportamento para estes casos.
    """
    def atuar(self):
        

        simboloAtual = self.fita.ler()
        transicao = self.estadoAtual.obterTransicao(simboloAtual)
        
        executouTransicao = transicao is not None
        if executouTransicao:
            print("Transição: ", transicao)
            print("Fita: ", self.fita)
            self.estadoAtual = transicao.destino
            self.fita.escrever(transicao.escrita)
            self.fita.mover(transicao.direcao)

        if executouTransicao and self.__verificaLoop():
            raise Exception(
                "[Maquina::atuar]: Foi identificado a partir de heurísticas que este programa está em loop.")

        return executouTransicao

    """
        Define a entrada da máquina, que deverá ser processada.
    """
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
    
    """
        Verificação contídua na heurística do problema da parada
    """
    def __verificaLoop(self):
        indiceEstadoAtual = 0

        for estado in self.estados:
            if estado == self.estadoAtual:
                break
            indiceEstadoAtual += 1

        # define a situação que a máquina se encontra
        # a posição atual de sua cabeça de leitura e o conteúdo presente na fita
        situacaoAtual = {self.fita.getPosicao(): self.fita.getConteudo()}
        
        if situacaoAtual in self.historico[indiceEstadoAtual]:
            return True
        
        # salva o estado (índice) no histórico e grava consigo a situação atual da fita
        self.historico[indiceEstadoAtual].append(situacaoAtual)
        return False
