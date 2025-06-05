def lcs(S, T):
    n, m = len(S), len(T)
    T_table = [[0] * (m + 1) for _ in range(n + 1)]  # Tabela DP

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:  # Caso 2
                T_table[i][j] = 1 + T_table[i - 1][j - 1]
            else:  # Caso 1
                T_table[i][j] = max(T_table[i - 1][j], T_table[i][j - 1])

    return T_table[n][m]  # Retorna o comprimento da LCS