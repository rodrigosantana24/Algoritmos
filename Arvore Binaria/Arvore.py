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
    
    def buscar(self, chave):
        if self.raiz == None:
            return None
        atual = self.raiz
        while atual.item != chave:
            if chave < atual.item:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
    
    def sucessor(self, apaga):
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.direita
        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != apaga.direita:
            paidosucessor.esquerda = sucessor.direita
            sucessor.direita = apaga.direita
        return sucessor
    
