def trocar(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def ordenar(lista, i, superior):
    while (True):
        l, r = i*2+1, i*2+2
        if max(l, r) < superior:
            if lista[i] >= max(lista[l], lista[r]): break
            elif lista[l] > lista[r]:
                trocar(lista, i, l)
                i = l
            else:
                trocar(lista, i, r)
                i = r
        elif l < superior:
            if lista[l] > lista[i]:
                trocar(lista, i, l)
                i = l
            else: break
        elif r < superior:          # parei aqui
            if lista[r] > lista[i]:
                trocar(lista, i, r)
                i = r
            else: break     
        else: break 

def heapsort(lista):
    for j in range((len(lista) - 2) // 2, -1, -1):
        ordenar(lista, j, len(lista))
    
    for end in range(len(lista) -1, 0, -1):
        trocar(lista, 0, end)
        ordenar(lista, 0, end)

lista = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]
heapsort(lista)
print(lista)