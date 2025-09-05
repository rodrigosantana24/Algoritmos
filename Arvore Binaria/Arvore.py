class No:
    def __init__(self, chave, esquerda, direita):
        self.item = chave
        self.esquerda = esquerda
        self.direita = direita
    
class Tree:
    def __init__(self):
        self.raiz = No(None, None, None)
        self.raiz = None
    
    def inserir(self, valor):
        novo = No(valor, None, None)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if valor <= atual.item:
                    atual = atual.esquerda
                    if atual == None:
                        anterior.esquerda = novo
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        anterior.direita = novo
                        return
    

