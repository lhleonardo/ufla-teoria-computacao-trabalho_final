from modulos.utils.colors import Color
from enum import Enum

"""
    Enumeração com todos os símbolos possíveis presentes no alfabeto
"""
class Simbolo(Enum):
    a = 1
    b = 2
    B = 3


"""
    Direções que uma fita pode mover-se
"""
class Direcao(Enum):
    ESQUERDA = 1
    DIREITA = 2

'''
    Classe que representa a fita de uma máquina de turing.

    A própria fita é auto capaz de realizar suas operações básicas, tais como
    mover sua cabeça de leitura/gravação, ler o conteúdo na posição que se encontra
    a cabeça de leitura e escrever na posição que se encontra a cabeça de gravação.

    Cada fita funciona independente de qualquer máquina.
'''
class Fita:
    def __init__(self):
        self.conteudo = [Simbolo.B, Simbolo.B]
        self.posicao = 0

    '''
        Retornar o símbolo presente no local que está posicionada
        a cabeça de leitura.
    '''
    def ler(self):
        return self.conteudo[self.posicao]

    '''
        Escrever o símbolo informado na posição 
    '''
    def escrever(self, simbolo):
        self.conteudo[self.posicao] = simbolo

    """
        Move o ponteiro de leitura/escrita da fita para uma determinada direção (ESQUERDA ou DIREITA)
    """
    def mover(self, direcao):
        if direcao == Direcao.DIREITA:
            self.posicao = self.posicao + 1
        else:
            self.posicao = self.posicao - 1

        # sempre colocar um Branco na última posição, caso extrapolar 
        # o tamanho da lista que representa o conteudo atual da fita
        if self.posicao == len(self.conteudo):
            self.conteudo.append(Simbolo.B)

    """
        Representação da fita para a saída padrão. Cor vermelha simboliza posição que se encontra.
    """
    def __repr__(self):
        string = "["
        atual = 0
        for simbolo in self.conteudo:
            if atual == self.posicao:
                string += Color.RED

            if simbolo == Simbolo.a:
                string += " a "
            elif simbolo == Simbolo.b:
                string += " b "
            else:
                string += " B "

            if atual == self.posicao:
                string += Color.END

            string += "|"
            atual = atual + 1

        string += "...]"

        return string

    def getConteudo(self):
        return self.conteudo
    def getPosicao(self):
        return self.posicao
