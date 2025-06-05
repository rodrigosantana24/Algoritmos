def mochila_booleana(capacidade, pesos, valores):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]  # Inicializa a matriz

    # Preenchimento da matriz
    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            if pesos[i - 1] <= j:
                dp[i][j] = max(valores[i - 1] + dp[i - 1][j - pesos[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacidade]  # Valor máximo