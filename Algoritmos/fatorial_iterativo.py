def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
n = int(input())
print(f"O fatorial de {n} é {fatorial_iterativo(n)}")


