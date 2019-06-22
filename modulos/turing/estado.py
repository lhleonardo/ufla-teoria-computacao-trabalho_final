class Transicao:
    def __init__(self, origem, leitura, destino, escrita, direcao):
        self.origem = origem
        self.leitura = leitura
        self.destino = destino
        self.escrita = escrita
        self.direcao = direcao

    def __repr__(self):
        return "[{0},{1}]=>[{2}, {3}, {4}]".format(self.origem, self.leitura, self.destino, self.escrita, self.direcao)


class Estado:
    def __init__(self, representacao):
        self.representacao = representacao
        self.transicoes = []

    def adicionaTransicao(self, leitura, destino, escrita, direcao):
        self.transicoes.append(
            Transicao(self, leitura, destino, escrita, direcao))

    def obterTransicao(self, simboloLido):
        for transicao in self.transicoes:
            if transicao.leitura == simboloLido:
                transicao.origem = self
                return transicao

        return None

    def __repr__(self):
        return "{0}".format(self.representacao)
