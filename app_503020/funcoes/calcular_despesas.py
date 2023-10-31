def calcular_despesas(valor):

    despesas_essenciais = valor * 0.5
    metas_financeiras = valor * 0.3
    despesas_estilo_vida = valor * 0.2

    # Cálculo das subcategorias das despesas essenciais
    aluguel = despesas_essenciais * 0.5
    contas = despesas_essenciais * 0.3
    alimentacao = despesas_essenciais * 0.2

    # Cálculo das subcategorias das metas financeiras
    poupanca = metas_financeiras * 0.5
    investimentos = metas_financeiras * 0.5

    # Cálculo das subcategorias das despesas de estilo de vida
    entretenimento = despesas_estilo_vida * 0.4
    lazer = despesas_estilo_vida * 0.3
    compras = despesas_estilo_vida * 0.3

    print("Aluguel:", aluguel)
    print("Contas:", contas)
    print("Alimentação:", alimentacao)
    print("Poupança:", poupanca)
    print("Investimentos:", investimentos)
    print("Entretenimento:", entretenimento)
    print("Lazer:", lazer)
    print("Compras:", compras)

