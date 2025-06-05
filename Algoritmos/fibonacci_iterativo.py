def fibonacci_iterativo(n):
    if n < 2:
        return n
    a, b, r = 0, 1, 1
    for _ in range(2, n+1):
        r = a+b
        a, b = b, r
        print(r, end=" ")    
    return ""

print(fibonacci_iterativo(5))
