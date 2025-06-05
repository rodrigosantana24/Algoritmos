class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._size = 0

    def inserir(self, elemento):
        # insere um elemento na pilha
        no = No(elemento)
        if self.ultimo is None:
            self.ultimo = no
        else:
            self.ultimo.proximo = no
            self.ultimo = no
        
        if self.primeiro is None:
            self.primeiro = no
        
        self._size = self._size + 1
    
    def remover(self, elemento):
        # remove o elemento do topo da pilha
        if self._size > 0:
            elemento = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
            self._size = self._size - 1
            return elemento
        raise IndexError("The queue is empty")
        
    def checar(self):
        # retorna o topo sem remover
        if self._size > 0:
            elemento = self.primeiro.dado
            return elemento
        raise IndexError("The queue is empty")
        

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

if __name__=='__main__':
    teste = Fila()
    teste.inserir(['teste', 'teste'])
    print(teste.checar())
    print(teste.checar())
    