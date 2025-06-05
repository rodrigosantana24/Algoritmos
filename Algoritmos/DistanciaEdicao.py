def distancia_edicao(S, T):
    m, n = len(S), len(T)
    M = [[0] * (n + 1) for _ in range(m + 1)]  # Inicializa a matriz

    # Inicialização das bordas da matriz
    for i in range(m + 1):
        M[i][0] = i  # Transformar S[1..i] em string vazia
    for j in range(n + 1):
        M[0][j] = j  # Transformar string vazia em T[1..j]

    # Preenchimento da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:  # Caracteres iguais
                c = 0
            else:  # Caracteres diferentes
                c = 1
            M[i][j] = min(
                M[i - 1][j - 1] + c,  # Substituição ou correspondência
                M[i - 1][j] + 1,       # Remoção
                M[i][j - 1] + 1        # Inserção
            )

    return M[m][n]  # Distância de edição entre S e T