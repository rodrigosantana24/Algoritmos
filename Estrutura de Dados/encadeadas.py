class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self._tamanho = 0
    
    def append(self, elemento):
        if self.head:
            # inserção quando a lista já possui elementos
            ponteiro = self.head
            while (ponteiro.proximo):
                ponteiro = ponteiro.proximo
            
            ponteiro.proximo = No(elemento)
        
        else:
            # primeira adição
            self.head = No(elemento)
        self._tamanho = self._tamanho + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._tamanho
    
    def _getNo(self, index):
        ponteiro = self.head
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("list index out of range")
        return ponteiro

    def __getitem__(self, index, elemento):
        # a = Lista[6]
        ponteiro = self._getNo(index)

        if ponteiro:
            return ponteiro.dado
        else:
            raise IndexError("list index out of range")    
        
    def __setitem__(self, index, elemento):
        # Lista[5] = 9
        ponteiro = self._getNo(index)
        if ponteiro:
            ponteiro.dado = elemento
        else:
            raise IndexError("list index out of range")
        
    def index(self, elemento):
        """retorna o índice do elemento na lista"""
        ponteiro = self.head
        i=0

        while (ponteiro):
            if ponteiro.dado == elemento:
                return i
            ponteiro = ponteiro.proximo
            i = i+1

        raise ValueError(f"{elemento} is not in list")

    def inserir(self, index, elemento):
        if index == 0:
            no = No(elemento)
            no.proximo = self.head
            self.head = no
        else:
            ponteiro = self._getNo(index - 1)
            no = No(elemento)
            ponteiro.proximo = no
        self._tamanho = self._tamanho + 1

    def remover(self, elemento):
        if self.head.dado == elemento:
            self.head = self.head.proximo
        else:       
            antecessor = self.head
            ponteiro = self.head.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    #remove
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
            self._tamanho = self._tamanho - 1
            return True
        raise ValueError(f"{elemento} is not in list")
                

lista = ListaEncadeada()
lista.append(7)
print(lista._tamanho)
lista.append(8)
print(lista._tamanho)