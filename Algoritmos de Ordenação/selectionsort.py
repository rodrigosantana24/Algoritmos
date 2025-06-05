def seletion_sort(lista):
    for j in range(len(lista) - 1):
        minimo_index = j
        
        for i in range(j, len(lista)):
            if lista[i] < lista[minimo_index]:
                minimo_index = i
        
        if lista[j] > lista[minimo_index]:
            auxiliar = lista[j]
            lista[j] = lista[minimo_index]
            lista[minimo_index] = auxiliar
    
    print(lista)

lista = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

seletion_sort(lista)