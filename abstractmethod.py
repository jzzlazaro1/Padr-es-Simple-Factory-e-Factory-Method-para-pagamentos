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

print("\033[31m classe abstrata: 'Pagamento', 'PagamentoCartao', 'PagamentoBoleto', 'PagamentoPix' está definido. \033")
