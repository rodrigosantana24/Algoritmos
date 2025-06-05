def plantacao_caju():
    # Lê a primeira linha da entrada e divide em uma lista de strings
    primeira_linha = input().split()
    linhas = int(primeira_linha[0])
    colunas = int(primeira_linha[1])
    M = int(primeira_linha[2])
    N = int(primeira_linha[3])

    # Lê as próximas 'linhas' linhas para construir a matriz
    matriz = []
    for _ in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Inicializa a matriz de soma prefixa com (linhas + 1) linhas e (colunas + 1) colunas preenchidas com 0s
    prefixo = [[0] * (colunas + 1) for _ in range(linhas + 1)]
    for i in range(1, linhas + 1):
        for j in range(1, colunas + 1):
            prefixo[i][j] = matriz[i - 1][j - 1] + prefixo[i - 1][j] + prefixo[i][j - 1] - prefixo[i - 1][j - 1]

    soma_maxima = 0
    for i in range(linhas - M + 1):
        for j in range(colunas - N + 1):
            x1 = i
            y1 = j
            x2 = i + M - 1
            y2 = j + N - 1
            soma_atual = prefixo[x2 + 1][y2 + 1] - prefixo[x1][y2 + 1] - prefixo[x2 + 1][y1] + prefixo[x1][y1]
            if soma_atual > soma_maxima:
                soma_maxima = soma_atual

    print(soma_maxima)

if __name__ == "__main__":
    plantacao_caju()