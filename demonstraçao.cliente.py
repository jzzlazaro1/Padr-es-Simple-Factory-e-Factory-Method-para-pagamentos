print('\033[35m--- Demonstração do Cliente com Abstract Factory ---\033')

# 1. Crie uma instancia de FactoryPagamentoOnline.
factory_online = FactoryPagamentoOnline()

# 2. Usando a instancia de FactoryPagamentoOnline, crie um objeto de pagamento para 'cartao' e um para 'pix'.
pagamento_cartao = factory_online.criarPagamento("cartao")
pagamento_pix = factory_online.criarPagamento("pix")

# 3. Chame o metodo processarPagamento para cada um dos objetos de pagamento online criados, passando um valor de sua escolha.
valor_online = 100.00
resultado_cartao = pagamento_cartao.processarPagamento(valor_online)
resultado_pix = pagamento_pix.processarPagamento(valor_online)

# 4. Crie uma instancia de FactoryPagamentoOffline.
factory_offline = FactoryPagamentoOffline()

# 5. Usando a instancia de FactoryPagamentoOffline, crie um objeto de pagamento para 'boleto'.
pagamento_boleto = factory_offline.criarPagamento("boleto")

# 6. Chame o metodo processarPagamento para o objeto de pagamento offline criado, passando um valor de sua escolha.
valor_offline = 50.50
resultado_boleto = pagamento_boleto.processarPagamento(valor_offline)

# 7. Imprima os resultados de cada chamada a processarPagamento para demonstrar o funcionamento.
print(f"\nPagamento Online (Cartão): {resultado_cartao}")
print(f"Pagamento Online (Pix): {resultado_pix}")
print(f"Pagamento Offline (Boleto): {resultado_boleto}") #como exemplo

print('\033[32m Demonstração concluída.\033')
