from modulos.turing.maquina import Maquina
from modulos.turing.fita import Fita, Simbolo, Direcao
from modulos.turing.estado import Estado, Transicao

# def validarEntrada(palavra):
#     expressao = r"(000)(((1+)(0)(1+)(0)(1+)(0)(1+)(0)(1+)00))*((1+)(0)(1+)(0)(1+)(0)(1+)(0)(1+))(000)(1+)(01+)*(000)"

#     return re.matches(expressao, palavra)
# def main():
#     nomeArquivo = input("Digite o local do arquivo: ")

#     arquivo = open(nomeArquivo, "r")

#     leitura = arquivo.readline()

#     if not validarEntrada(leitura):
#         raise Exception("Representação da maquina inválida.")


def main():
    m1 = Maquina()

    q0 = Estado("q0")
    q1 = Estado("q1")
    q2 = Estado("q2")
    q3 = Estado("q3")
    q4 = Estado("q4")
    q5 = Estado("q5")
    q6 = Estado("q6")

    q0.adicionaTransicao(leitura=Simbolo.B, destino=q1,
                         escrita=Simbolo.B, direcao=Direcao.DIREITA)

    q1.adicionaTransicao(leitura=Simbolo.a, destino=q2,
                         escrita=Simbolo.a, direcao=Direcao.DIREITA)
    q1.adicionaTransicao(leitura=Simbolo.b, destino=q6,
                         escrita=Simbolo.b, direcao=Direcao.DIREITA)

    q2.adicionaTransicao(leitura=Simbolo.a, destino=q4,
                         escrita=Simbolo.a, direcao=Direcao.DIREITA)

    q4.adicionaTransicao(leitura=Simbolo.b, destino=q5,
                         escrita=Simbolo.b, direcao=Direcao.ESQUERDA)

    q5.adicionaTransicao(leitura=Simbolo.a, destino=q1,
                         escrita=Simbolo.a, direcao=Direcao.ESQUERDA)                                         

    m1.adicionaEstado(q0, inicial=True)
    m1.adicionaEstado(q1)
    m1.adicionaEstado(q2)
    m1.adicionaEstado(q3)
    m1.adicionaEstado(q4)
    m1.adicionaEstado(q5)

    m1.setEntrada("aab")

    i = 1
    while m1.atuar():
        print("A máquina executou ", i, " vez(es)")
        i = i + 1

main()
