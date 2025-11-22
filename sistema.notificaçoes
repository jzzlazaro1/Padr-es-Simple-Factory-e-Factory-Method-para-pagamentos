from abc import ABC, abstractmethod
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, destino: str, mensagem: str) -> str:
        pass

class NotificacaoFactory(ABC):
    @abstractmethod
    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        pass

print("Classe abstrata 'NotificacaoFactory' e o seu método abstrato 'criarNotificacao' estão definidos.")
