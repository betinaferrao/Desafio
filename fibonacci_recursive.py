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

def solicitar_numero():
    while True:
        n = int(input('Quantos termos da sequência de Fibonacci você deseja visualizar? '))
        if n >= 0:
            return n
        else:
            print("Por favor, insira um número maior ou igual a zero.")

n = solicitar_numero()
print_sequencia(n)