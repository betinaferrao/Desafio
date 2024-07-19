def fibonacci_linear(n):
    num1 = 0
    num2 = 1
    print('{} -> {}'.format(num1,num2), end='')
    aux = 3
    while aux <= n:
        soma = num1 + num2
        print(' -> {}'.format(soma), end='')
        num1 = num2
        num2 = soma
        aux += 1

n = int(input('Quantos termos da sequência de Fibonacci você deseja visualizar? '))
fibonacci_linear(n)

