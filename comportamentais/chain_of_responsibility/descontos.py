class DescontoCincoItens:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        print(f'DescontoCincoItens: {orcamento.total_itens}')
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        return self.__proximo_desconto.calcula(orcamento)


class DescontoMaisDeQuinhentosReais:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        print(f'DescontoMaisDeQuinhentosReais: {orcamento.valor}')
        if orcamento.valor > 500.0:
            return orcamento.valor * 0.07
        return self.__proximo_desconto.calcula(orcamento)


class SemDesconto:
    def calcula(self, orcamento):
        print(f'SemDesconto: {orcamento.valor}')
        return 0
