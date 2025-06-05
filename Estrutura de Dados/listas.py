class Lista:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def inserir(self, indice, valor):
        if indice < 0 or indice > self.tamanho():
            raise IndexError("Índice fora do intervalo")
        self.itens.insert(indice, valor)

    def remover(self, indice):
        if self.esta_vazia():
            raise IndexError("A lista está vazia")
        if indice < 0 or indice >= self.tamanho():
            raise IndexError("Índice fora do intervalo")
        return self.itens.pop(indice)

    def buscar(self, indice):
        if indice < 0 or indice >= self.tamanho():
            raise IndexError("Índice fora do intervalo")
        return self.itens[indice]

    def __str__(self):
        return str(self.itens)





# Exemplo de uso
minha_lista = Lista()
print("Lista vazia?", minha_lista.esta_vazia())  # True

minha_lista.inserir(0, 10)
minha_lista.inserir(1, 20)
minha_lista.inserir(2, 30)
print("Lista após inserções:", minha_lista)  # [10, 20, 30]

print("Tamanho da lista:", minha_lista.tamanho())  # 3

print("Elemento na posição 1:", minha_lista.buscar(1))  # 20

minha_lista.remover(1)
print("Lista após remoção:", minha_lista)  # [10, 30]

print("Lista vazia?", minha_lista.esta_vazia())  # False