# inserir, remover e observar o topo da pilha.
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        

class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho = 0

    def inserir(self, elemento):
        # insere um elemento na pilha
        no = No(elemento)
        no.proximo = self.topo
        self.topo = no
        self._tamanho = self._tamanho + 1

    def remover(self):
        # remove o elemento do topo da pilha
        if self._tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self._tamanho = self._tamanho - 1
            return no
        raise IndexError("The stack is empty")

    def checar(self):
        # retorna o topo da pilha sem remover
        if self._tamanho > 0:
            return self.topo.dado        
        raise IndexError("The stack is empty")
        

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._tamanho 