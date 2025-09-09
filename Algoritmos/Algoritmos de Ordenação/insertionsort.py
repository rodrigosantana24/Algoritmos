def insertion_sort(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        for i in range(1, n):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                lista[j+1] = lista[j]
                j = j - 1
            lista[j+1] = chave


lista = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

insertion_sort(lista)

print(lista)
