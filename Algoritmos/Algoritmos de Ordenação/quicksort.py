def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio

    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i+1
    
    lista[i], lista[fim] = lista [fim], lista[i]
    
    return i

lista = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

quicksort(lista)
print(lista)