import math
from despesa import Despesa


class Calculo():
    def __init__(self) -> None:
        pass

    def captura_decimais(self, f, n):
        return math.floor(f * 10 ** n) / 10 ** n

    def funcao(self, lista_despesas, lista_nomes):
        dicionario = {}
        total = 0
        if len(lista_nomes) == 0:
            return 'Não há pessoas para dividir'

        if len(lista_despesas) == 0:
            return 'Não há despesas'

        for i in lista_despesas:
            total += i.qtd * i.preco_por_unidade * 100

        if total == 0:
            return 'Ninguém está devendo'

        if (total % len(lista_nomes)) == 0:
            for nome in lista_nomes:
                dicionario[nome] = total / len(lista_nomes) / 100
            return dicionario

        else:
            div_arred = total/len(lista_nomes)

            distrib = total % len(lista_nomes)
            for nome in lista_nomes:
                dicionario[nome] = div_arred
            for i in range(0, int(distrib)):
                dicionario[lista_nomes[i]] += 1
            for nome in lista_nomes:

                dicionario[nome] = self.captura_decimais(
                    dicionario[nome] / 100, 2)
            return dicionario
