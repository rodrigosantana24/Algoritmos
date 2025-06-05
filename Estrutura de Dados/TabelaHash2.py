class Elemento:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

    def __repr__(self):
        return f"({self.chave}: {self.valor})"


class TabelaHashSimples:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.tabela = [[] for _ in range(capacidade)]  # Lista de listas para tratar colisões
        self.tamanho = 0  # Quantidade de elementos na tabela

    def __len__(self):
        return self.tamanho

    def funcao_hash(self, chave):
        """
        Função hash simples que usa o valor hash da chave e aplica módulo.
        :param chave: A chave a ser transformada em hash.
        :return: O índice calculado.
        """
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        """
        Insere ou atualiza um elemento na tabela hash.
        :param chave: A chave do elemento.
        :param valor: O valor do elemento.
        """
        indice = self.funcao_hash(chave)
        for elemento in self.tabela[indice]:
            if elemento.chave == chave:
                elemento.valor = valor  # Atualiza o valor se a chave já existir
                return
        self.tabela[indice].append(Elemento(chave, valor))  # Adiciona novo elemento
        self.tamanho += 1

    def buscar(self, chave):
        """
        Busca um elemento na tabela hash.
        :param chave: A chave do elemento.
        :return: O valor associado à chave.
        :raises KeyError: Se a chave não for encontrada.
        """
        indice = self.funcao_hash(chave)
        for elemento in self.tabela[indice]:
            if elemento.chave == chave:
                return elemento.valor
        raise KeyError(f"Chave '{chave}' não encontrada")

    def remover(self, chave):
        """
        Remove um elemento da tabela hash.
        :param chave: A chave do elemento.
        :raises KeyError: Se a chave não for encontrada.
        """
        indice = self.funcao_hash(chave)
        for i, elemento in enumerate(self.tabela[indice]):
            if elemento.chave == chave:
                del self.tabela[indice][i]  # Remove o elemento
                self.tamanho -= 1
                return
        raise KeyError(f"Chave '{chave}' não encontrada")

    def __repr__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.tabela))


# Exemplo de uso
tabela = TabelaHashSimples()

# Inserindo elementos
tabela.inserir("chave1", "valor1")
tabela.inserir("chave2", "valor2")
tabela.inserir("chave3", "valor3")

# Acessando elementos
print("Valor da chave1:", tabela.buscar("chave1"))
print("Valor da chave2:", tabela.buscar("chave2"))

# Removendo elementos
tabela.remover("chave2")

# Tentando acessar uma chave removida (lança KeyError)
try:
    print("Valor da chave2:", tabela.buscar("chave2"))
except KeyError as e:
    print(e)

# Exibindo a tabela hash
print("\nTabela Hash:")
print(tabela)