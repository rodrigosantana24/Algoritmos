def criar_tabela_auxiliar(fazenda, L, C):
    # alocar a tabela auxiliar
    tabela = [[0 for _ in range(C+1)] for _ in range(L+1)]

    for i in range(1, L+1):
        for j in range(1, C+1):
            tabela[i][j] = tabela[i-1][j] + tabela[i][j-1] - tabela[i-1][j-1] + tabela[i-1][j-1]
    
    return tabela

def colher_caju(fazenda, L, C, M, N):
    tabela_auxiliar = criar_tabela_auxiliar(fazenda, L, C)
    for i in range(M, C+1):
        for j in range(N, L+1):
            pass

        
    return tabela_auxiliar



def ler_entrada():
    # lendo os tamanhos das areas
    L, C, M, N = [int(i) for i in input().split()]

    # lendo as fazendas
    fazenda = [int(j) for j in input().split() for _ in range(L)]
    tabela_auxiliar = criar_tabela_auxiliar(fazenda)

    return fazenda


def principal():
    pass