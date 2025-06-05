class Elemento:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor


class TabelaHash:
    def __init__(self):
        self.capacidade_atual = 5 # Capacidade da tabela interna
        self.tabela_interna = [[] for _ in range(self.capacidade_atual)]
        self.tamanho = 0   # Quantidade de elementos salvos na tabela hash

    def __len__(self):
        return self.tamanho
    
    def funcao_hash(chave):
        pass

    def index(self, chave):
        hash(chave) % self.capacidade_atual

    def __SetItem__(self, chave, valor):
        indice = self.index(chave)


pessoa1 = TabelaHash()
pessoa1["Nome:"] = "Rodrigo"
pessoa1["idade:"] = 23
pessoa1["Sexo:"] = "M"
pessoa1["Profissão:"] = "Programador"
pessoa1["Nacionalidade:"] = "Brasileiro"
pessoa1["Salário"] = 1400.00