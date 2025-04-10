def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    top_esquerda, top_direita = 0, 0
    
    for k in range(inicio, fim):
        if top_esquerda >= len(esquerda):
            lista[k] = direita[top_direita]
            top_direita = top_direita + 1
        
        elif top_direita >= len(direita):
            lista[k] = esquerda[top_esquerda]
            top_esquerda = top_esquerda + 1
        
        elif esquerda[top_esquerda] < direita[top_direita]:
            lista[k] = esquerda[top_esquerda]
            top_esquerda = top_esquerda + 1
        
        else:
            lista[k] = direita[top_direita]
            top_direita = top_direita + 1

lista = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

mergesort(lista)
print(lista)


