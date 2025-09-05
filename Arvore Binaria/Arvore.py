class No:
    def __init__(self, chave, esquerda, direita):
        self.item = chave
        self.esquerda = esquerda
        self.direita = direita
    
class Tree:
    def __init__(self):
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
    
    def remover(self, valor):
        if self.raiz == None:
            return False
        atual = self.raiz
        pai = self.raiz
        filho_esquerdo = True
        while atual.item != valor:
            pai = atual
            if valor < atual.item:
                filho_esquerdo = True
                atual = atual.esquerda
            else:
                filho_esquerdo = False
                atual = atual.direita
            if atual == None:
                return False
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    pai.esquerda = None
                else:
                    pai.direita = None
        elif atual.direita == None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            else:
                if filho_esquerdo:
                    pai.esquerda = atual.esquerda
                else:
                    pai.direita = atual.esquerda
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            else:
                if filho_esquerdo:
                        pai.esquerda = atual.direita 
                else:
                        pai.direita = atual.direita 
        else:
            sucessor = self.sucessor(atual)
            if atual == self.raiz:
                    self.raiz = sucessor 
            else:
                    if filho_esquerdo:
                        pai.esquerda = sucessor 
                    else:
                        pai.direita = sucessor 
            sucessor.esquerda = atual.esquerda 
        return True
    
    def precessor(self, no):
        pai_do_precessor = no
        precessor = no
        atual = no.esquerda
        while atual is not None:
            pai_do_precessor = precessor
            precessor = atual
            atual = atual.direita
        if precessor != no.esquerda:
            pai_do_precessor.direita = precessor.esquerda
            precessor.esquerda = no.esquerda
        return precessor

    def min(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esquerda
        return anterior
    
    def max(self):
        atual = self.root
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.dir
        return anterior


