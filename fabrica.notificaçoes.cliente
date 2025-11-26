from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, destino: str, mensagem: str) -> str:
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"E-mail enviado para {destino} com a mensagem: '{mensagem}'."

class NotificacaoSMS(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"SMS enviado para {destino} com a mensagem: '{mensagem}'."

class NotificacaoWhatsApp(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"Mensagem de WhatsApp enviada para {destino} com a mensagem: '{mensagem}'."

class NotificacaoFactory(ABC):
    @abstractmethod
    def criarNotificacao(self) -> Notificacao:
        pass

class EmailNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoEmail()

class SMSNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoSMS()

class WhatsAppNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoWhatsApp()


print('\033[35m--- Demonstração do Cliente com Fábricas Concretas de Notificação ---\033')

# 1. Crie instâncias das fábricas concretas
email_factory = EmailNotificacaoFactory()
sms_factory = SMSNotificacaoFactory()
whatsapp_factory = WhatsAppNotificacaoFactory()

# 2. Use as fábricas para criar objetos de notificação e enviar mensagens

# Criar e enviar notificação por e-mail
email_notifier = email_factory.criarNotificacao()
print(email_notifier.enviar("cliente@exemplo.com", "Sua fatura mensal está disponível."))

# Criar e enviar notificação por SMS
sms_notifier = sms_factory.criarNotificacao()
print(sms_notifier.enviar("+559988776655", "Seu pedido foi despachado!"))

# Criar e enviar notificação por WhatsApp
whatsapp_notifier = whatsapp_factory.criarNotificacao()
print(whatsapp_notifier.enviar("+5511999998888", "Promoção exclusiva para você!"))

print('\033[32m Demonstração das Fábricas de Notificação concluída.\033')
