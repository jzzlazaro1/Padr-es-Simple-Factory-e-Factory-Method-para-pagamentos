from abc import ABC, abstractmethod
class Pagamento(ABC):
    @abstractmethod
    def processarPagamento(self, valor: float) -> str:
        pass
class PagamentoCartao(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com cartão de crédito."

class PagamentoBoleto(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com boleto bancário."
class PagamentoPix(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com Pix."
class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        pass
class FactoryPagamentoOnline(PagamentoFactory):
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        if tipo_pagamento == "cartao":
            return PagamentoCartao()
        elif tipo_pagamento == "pix":
            return PagamentoPix()
        else:
            raise ValueError(f"Tipo de pagamento online não suportado: {tipo_pagamento}")
class FactoryPagamentoOffline(PagamentoFactory):
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        if tipo_pagamento == "boleto":
            return PagamentoBoleto()
        else:
            raise ValueError(f"Tipo de pagamento offline não suportado: {tipo_pagamento}")
          
print("\033[32m Classes 'FactoryPagamentoOnline' e 'FactoryPagamentoOffline' implementadas com sucesso \033")
