def fibonacci_recursiva(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursiva(n - 2) + fibonacci_recursiva(n - 1)

def print_sequencia(n):
    for i in range(n):
        print(fibonacci_recursiva(i), end=' -> ' if i < n - 1 else '\n')

n = int(input('Quantos termos da sequência de Fibonacci você deseja visualizar? '))
print_sequencia(n)