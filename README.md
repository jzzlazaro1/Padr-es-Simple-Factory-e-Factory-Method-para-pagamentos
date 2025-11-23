🏭 **Abstract Factory & Strategy em Python**

Uma implementação de sistema que utiliza os padrões de design Abstract Factory e Strategy para criar e gerenciar diferentes métodos de pagamento e canais de notificação de forma flexível e extensível.

🌟 **Padrões de Design**

Este projeto exemplifica a aplicação de:

1. Strategy Pattern (Estratégia)
Onde: Classes Pagamento e Notificacao.

O que faz: Define uma família de algoritmos, encapsula cada um e os torna intercambiáveis.

Em Pagamento, permite trocar facilmente entre Cartão, Pix ou Boleto.

Em Notificacao, permite trocar facilmente entre E-mail, SMS ou WhatsApp.

2. Abstract Factory Pattern (Fábrica Abstrata)
Onde: Classes PagamentoFactory e NotificacaoFactory.

O que faz: Fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

Fábricas de Pagamento: Permitem criar objetos dentro da "família" Online (Cartão, Pix) ou Offline (Boleto).

Fábricas de Notificação: Permitem criar objetos específicos (Email, SMS, WhatsApp) de forma controlada.

⚙️ **Estrutura do Código (design_patterns_demo.py)**

Todo o sistema está contido em um único arquivo, demonstrando as interfaces abstratas e suas implementações concretas.

Python

from abc import ABC, abstractmethod

# =================================================================
# I. Padrão Strategy: Pagamento
# =================================================================

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

# =================================================================
# II. Padrão Strategy: Notificação
# =================================================================

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

# =================================================================
# III. Padrão Abstract Factory: FÁBRICAS DE NOTIFICAÇÃO
# (Aplicando o padrão Factory Method para Notificação)
# =================================================================

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


# =================================================================
# IV. Padrão Abstract Factory: FÁBRICAS DE PAGAMENTO
# (Aplicando o padrão Abstract Factory para a família Pagamento)
# =================================================================

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

# =================================================================
# V. Demonstrações do Cliente
# =================================================================

def demonstracao_notificacao():
    print('\n--- Demonstração: Fábricas de Notificação ---')

    email_factory = EmailNotificacaoFactory()
    sms_factory = SMSNotificacaoFactory()
    whatsapp_factory = WhatsAppNotificacaoFactory()

    # Criar e enviar notificação por e-mail
    email_notifier = email_factory.criarNotificacao()
    print(email_notifier.enviar("cliente@exemplo.com", "Sua fatura mensal está disponível."))

    # Criar e enviar notificação por SMS
    sms_notifier = sms_factory.criarNotificacao()
    print(sms_notifier.enviar("+559988776655", "Seu pedido foi despachado!"))

    # Criar e enviar notificação por WhatsApp
    whatsapp_notifier = whatsapp_factory.criarNotificacao()
    print(whatsapp_notifier.enviar("+5511999998888", "Promoção exclusiva para você!"))

def demonstracao_pagamento():
    print('\n--- Demonstração: Abstract Factory de Pagamento ---')

    # 1. Pagamento Online (Família Online)
    factory_online = FactoryPagamentoOnline()
    pagamento_cartao = factory_online.criarPagamento("cartao")
    pagamento_pix = factory_online.criarPagamento("pix")

    valor_online = 100.00
    print(pagamento_cartao.processarPagamento(valor_online))
    print(pagamento_pix.processarPagamento(valor_online))

    # 2. Pagamento Offline (Família Offline)
    factory_offline = FactoryPagamentoOffline()
    pagamento_boleto = factory_offline.criarPagamento("boleto")

    valor_offline = 50.50
    print(pagamento_boleto.processarPagamento(valor_offline))

if __name__ == "__main__":
    demonstracao_notificacao()
    demonstracao_pagamento()
    
🚀 **Como Executar**

O projeto é um único arquivo Python e requer apenas o interpretador Python instalado.

Pré-requisitos
Python 3.x

Passos
Salve o código acima em um arquivo chamado design_patterns_demo.py.

Execute o arquivo a partir do seu terminal:

Bash

python design_patterns_demo.py
Saída Esperada
--- Demonstração: Fábricas de Notificação ---
E-mail enviado para cliente@exemplo.com com a mensagem: 'Sua fatura mensal está disponível.'.
SMS enviado para +559988776655 com a mensagem: 'Seu pedido foi despachado!'.
Mensagem de WhatsApp enviada para +5511999998888 com a mensagem: 'Promoção exclusiva para você!'.

--- Demonstração: Abstract Factory de Pagamento ---
Pagamento de R$100.00 realizado com cartão de crédito.
Pagamento de R$100.00 realizado com Pix.
Pagamento de R$50.50 realizado com boleto bancário.



