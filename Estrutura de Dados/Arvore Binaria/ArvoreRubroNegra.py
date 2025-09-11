VERMELHO = "VERMELHO"
PRETO = "PRETO"

class No:
    """
    Representa um nó na Árvore Rubro-Negra.
    Além do valor (chave), contém atributos para cor, pai, filho esquerdo e direito.
    """
    def __init__(self, chave, cor=VERMELHO, pai=None, esquerda=None, direita=None):
        self.chave = chave
        self.cor = cor
        self.pai = pai
        self.esquerda = esquerda
        self.direita = direita

class ArvoreVermelhaPreta:
    """
    Implementação da Árvore Rubro-Negra baseada no livro do Cormen.
    """
    def __init__(self):
        # O nó sentinela T.nil representa todas as folhas da árvore.
        # Ele é sempre PRETO e seus ponteiros podem apontar para si mesmo.
        self.nil = No(chave=None, cor=PRETO)
        self.raiz = self.nil

    def rotacao_esquerda(self, x):
        """
        Executa uma rotação para a esquerda no nó x.
        Assume que x.direita não é T.nil.
        """
        y = x.direita
        x.direita = y.esquerda
        
        if y.esquerda != self.nil:
            y.esquerda.pai = x
            
        y.pai = x.pai
        
        if x.pai == self.nil:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
            
        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, y):
        """
        Executa uma rotação para a direita no nó y.
        Assume que y.esquerda não é T.nil.
        """
        x = y.esquerda
        y.esquerda = x.direita

        if x.direita != self.nil:
            x.direita.pai = y

        x.pai = y.pai

        if y.pai == self.nil:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x

        x.direita = y
        y.pai = x

    def inserir(self, chave):
        """
        Insere uma nova chave na árvore e chama o fixup para manter as propriedades.
        """
        # Cria um novo nó. A cor inicial é VERMELHO.
        z = No(chave=chave, cor=VERMELHO, pai=self.nil, esquerda=self.nil, direita=self.nil)
        
        y = self.nil
        x = self.raiz

        # Encontra a posição correta para inserir o novo nó, como em uma BST.
        while x != self.nil:
            y = x
            if z.chave < x.chave:
                x = x.esquerda
            else:
                x = x.direita

        z.pai = y
        if y == self.nil:
            self.raiz = z
        elif z.chave < y.chave:
            y.esquerda = z
        else:
            y.direita = z

        # Chama a função de correção para restaurar as propriedades Rubro-Negras.
        self.inserir_fixup(z)

    def inserir_fixup(self, z):
        """
        Corrige a árvore após a inserção para manter as propriedades Rubro-Negras.
        """
        while z.pai.cor == VERMELHO:
            # Caso A: O pai de z é um filho à esquerda do avô de z.
            if z.pai == z.pai.pai.esquerda:
                y = z.pai.pai.direita  # y é o "tio" de z.
                
                # Caso 1: O tio de z é VERMELHO.
                if y.cor == VERMELHO:
                    z.pai.cor = PRETO
                    y.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    z = z.pai.pai
                else:
                    # Caso 2: O tio de z é PRETO e z é um filho à direita.
                    if z == z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)
                    # Caso 3: O tio de z é PRETO e z é um filho à esquerda.
                    z.pai.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    self.rotacao_direita(z.pai.pai)
            # Caso B: O pai de z é um filho à direita do avô de z (simétrico ao Caso A).
            else:
                y = z.pai.pai.esquerda # y é o "tio" de z.

                # Caso 1 (simétrico): O tio de z é VERMELHO.
                if y.cor == VERMELHO:
                    z.pai.cor = PRETO
                    y.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    z = z.pai.pai
                else:
                    # Caso 2 (simétrico): O tio de z é PRETO e z é um filho à esquerda.
                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)
                    # Caso 3 (simétrico): O tio de z é PRETO e z é um filho à direita.
                    z.pai.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    self.rotacao_esquerda(z.pai.pai)
        
        # Garante que a raiz seja sempre PRETA (Propriedade 2).
        self.raiz.cor = PRETO

    def transplantar(self, u, v):
        """
        Substitui a subárvore enraizada em 'u' pela subárvore enraizada em 'v'.
        """
        if u.pai == self.nil:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def minimo_arvore(self, x):
        """Encontra o nó com a menor chave na subárvore de x."""
        while x.esquerda != self.nil:
            x = x.esquerda
        return x

    def remover(self, chave):
        """
        Encontra e remove um nó com a chave especificada.
        """
        z = self.buscar(chave)
        if z == self.nil:
            print(f"Nó com chave {chave} não encontrado.")
            return

        y = z
        y_cor_original = y.cor
        
        if z.esquerda == self.nil:
            x = z.direita
            self.transplantar(z, z.direita)
        elif z.direita == self.nil:
            x = z.esquerda
            self.transplantar(z, z.esquerda)
        else:
            y = self.minimo_arvore(z.direita)
            y_cor_original = y.cor
            x = y.direita
            if y.pai == z:
                x.pai = y
            else:
                self.transplantar(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y
            self.transplantar(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor
            
        if y_cor_original == PRETO:
            self.remover_fixup(x)

    def remover_fixup(self, x):
        """
        Corrige a árvore após a remoção para manter as propriedades Rubro-Negras.
        """
        while x != self.raiz and x.cor == PRETO:
            if x == x.pai.esquerda:
                w = x.pai.direita # w é o irmão de x
                # Caso 1: O irmão de x (w) é VERMELHO.
                if w.cor == VERMELHO:
                    w.cor = PRETO
                    x.pai.cor = VERMELHO
                    self.rotacao_esquerda(x.pai)
                    w = x.pai.direita
                
                # Caso 2: O irmão de x (w) é PRETO e ambos os filhos de w são PRETOS.
                if w.esquerda.cor == PRETO and w.direita.cor == PRETO:
                    w.cor = VERMELHO
                    x = x.pai
                else:
                    # Caso 3: O irmão de x (w) é PRETO, o filho esquerdo de w é VERMELHO e o direito é PRETO.
                    if w.direita.cor == PRETO:
                        w.esquerda.cor = PRETO
                        w.cor = VERMELHO
                        self.rotacao_direita(w)
                        w = x.pai.direita
                    # Caso 4: O irmão de x (w) é PRETO e o filho direito de w é VERMELHO.
                    w.cor = x.pai.cor
                    x.pai.cor = PRETO
                    w.direita.cor = PRETO
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else: # Simétrico se x é o filho direito
                w = x.pai.esquerda
                # Caso 1 (simétrico)
                if w.cor == VERMELHO:
                    w.cor = PRETO
                    x.pai.cor = VERMELHO
                    self.rotacao_direita(x.pai)
                    w = x.pai.esquerda
                
                # Caso 2 (simétrico)
                if w.direita.cor == PRETO and w.esquerda.cor == PRETO:
                    w.cor = VERMELHO
                    x = x.pai
                else:
                    # Caso 3 (simétrico)
                    if w.esquerda.cor == PRETO:
                        w.direita.cor = PRETO
                        w.cor = VERMELHO
                        self.rotacao_esquerda(w)
                        w = x.pai.esquerda
                    # Caso 4 (simétrico)
                    w.cor = x.pai.cor
                    x.pai.cor = PRETO
                    w.esquerda.cor = PRETO
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = PRETO

    def buscar(self, chave):
        """
        Busca por uma chave na árvore. Retorna o nó ou T.nil se não encontrar.
        """
        atual = self.raiz
        while atual != self.nil and chave != atual.chave:
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return atual

    def imprimir_in_order(self, no):
        """Imprime a árvore em ordem."""
        if no != self.nil:
            self.imprimir_in_order(no.esquerda)
            print(f"Chave: {no.chave}, Cor: {no.cor}")
            self.imprimir_in_order(no.direita)

if __name__ == "__main__":
    arvore = ArvoreVermelhaPreta()
    
    chaves = [11, 2, 14, 1, 7, 15, 5, 8]
    print(f"Inserindo as chaves: {chaves}\n")
    for chave in chaves:
        arvore.inserir(chave)

    print("--- Árvore em ordem ---")
    arvore.imprimir_in_order(arvore.raiz)
    print("-----------------------\n")

    print("Buscando pela chave 7...")
    no_encontrado = arvore.buscar(7)
    if no_encontrado != arvore.nil:
        print(f"Nó encontrado! Chave: {no_encontrado.chave}, Cor: {no_encontrado.cor}\n")
    else:
        print("Nó não encontrado.\n")

    chave_para_remover = 2
    print(f"Removendo a chave: {chave_para_remover}\n")
    arvore.remover(chave_para_remover)

    print("--- Árvore em ordem após a remoção ---")
    arvore.imprimir_in_order(arvore.raiz)
    print("------------------------------------")