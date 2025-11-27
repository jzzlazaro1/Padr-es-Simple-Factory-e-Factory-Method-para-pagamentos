🏗️ **Padrões de Criação em Python:**

Factory Method e Fábricas de PagamentoEste repositório em Python demonstra o uso de Padrões de Criação para gerenciar a instancialização de objetos em dois domínios distintos: Processamento de Pagamentos e Serviços de Notificação.

🚀 **Padrões Demonstrados**

Padrão,Domínio,Conceito Principal
Factory Method,Notificações,Delega a responsabilidade de criação para subclasses.
Fábrica Simples/Agrupada,Pagamentos,Centraliza a lógica de criação de produtos relacionados (Online vs. Offline) em classes especializadas.

💳**1. Padrão de Pagamento:**

Fábricas Agrupadas (FactoryPagamentoOnline, FactoryPagamentoOffline)

Este domínio demonstra uma abordagem para agrupar produtos relacionados (Pagamentos) em fábricas específicas. Embora a classe base PagamentoFactory defina um método de criação que se assemelha ao Factory Method, as implementações concretas (FactoryPagamentoOnline, FactoryPagamentoOffline) contêm lógica condicional que as torna uma variação do Simple Factory dentro de uma hierarquia de fábricas, o que é uma técnica comum que lembra o padrão Abstract Factory.Estrutura de PagamentosProduto Abstrato: Pagamento (com o método processarPagamento).

Estrutura de Pagamentos
Produto Abstrato: Pagamento (com o método processarPagamento).

Produtos Concretos: PagamentoCartao, PagamentoBoleto, PagamentoPix.

Fábricas Concretas:

FactoryPagamentoOnline: Cria PagamentoCartao ou PagamentoPix.

FactoryPagamentoOffline: Cria PagamentoBoleto.

Produtos Concretos: PagamentoCartao, PagamentoBoleto, PagamentoPix.
Fábricas Concretas: FactoryPagamentoOnline: 

Cria PagamentoCartao ou PagamentoPix.

FactoryPagamentoOffline: Cria PagamentoBoleto.

Trecho de Demonstração (Cliente)Python# Demonstração do Cliente com Abstract Factory (Exemplo)

factory_online = FactoryPagamentoOnline()
pagamento_cartao = factory_online.criarPagamento("cartao")
print(f"Pagamento Online (Cartão): {pagamento_cartao.processarPagamento(100.00)}")

factory_offline = FactoryPagamentoOffline()
pagamento_boleto = factory_offline.criarPagamento("boleto")
print(f"Pagamento Offline (Boleto): {pagamento_boleto.processarPagamento(50.50)}")

🔔 **2. Padrão de Notificação:** 

Factory MethodNo domínio de notificações, o padrão Factory Method é estritamente aplicado. Em vez de uma única classe de fábrica com if/else, existe uma hierarquia de fábricas, onde cada fábrica concreta é responsável por criar apenas um tipo de notificação.ShutterstockExplorarEstrutura de NotificaçãoProduto Abstrato: Notificacao (com o método enviar).

Produtos Concretos: NotificacaoEmail, NotificacaoSMS, NotificacaoWhatsApp.Fábricas Concretas: EmailNotificacaoFactory:

Cria NotificacaoEmail.SMSNotificacaoFactory: Cria NotificacaoSMS.WhatsAppNotificacaoFactory: Cria NotificacaoWhatsApp.Vantagem Principal (OCP)Este padrão segue o Princípio Aberto/Fechado (OCP). Para adicionar uma nova forma de notificação (ex: NotificacaoPush), basta criar a classe NotificacaoPush e sua fábrica correspondente, sem modificar as classes de fábrica existentes.

Trecho de Demonstração (Cliente)Python# Demonstração do Cliente com Fábricas Concretas

email_factory = EmailNotificacaoFactory()
email_notifier = email_factory.criarNotificacao()
print(email_notifier.enviar("cliente@exemplo.com", "Sua fatura mensal está disponível."))

sms_factory = SMSNotificacaoFactory()
sms_notifier = sms_factory.criarNotificacao()
print(sms_notifier.enviar("+559988776655", "Seu pedido foi despachado!"))

💻 **Como Rodar o Projeto (Python)Assumindo que você está utilizando Python 3:1.**

Clonar o RepositórioBashgit clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git
cd NomeDoSeuRepositorio

2. Executar se o seu código está em um único arquivo (main.py), basta executá-lo para ver a demonstração de ambos os padrões:Bashpython main.py

🛠️ **Detalhes da Implementação:**

Todas as classes abstratas utilizam o módulo abc do Python e o decorador @abstractmethod para garantir que as classes concretas implementem os métodos necessários (processarPagamento ou enviar).



