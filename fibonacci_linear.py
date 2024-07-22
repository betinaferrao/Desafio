def fibonacci_linear(n):
    num1 = 0
    num2 = 1
    if n == 0:
        print('Zero termos foram solicitados')
        return
    if n == 1:
        print(num1)
        return
    print('{} -> {}'.format(num1,num2), end='')
    aux = 3
    while aux <= n:
        soma = num1 + num2
        print(' -> {}'.format(soma), end='')
        num1 = num2
        num2 = soma
        aux += 1

def solicitar_numero():
    while True:
        n = int(input('Quantos termos da sequência de Fibonacci você deseja visualizar? '))
        if n >= 0:
            return n
        else:
            print("Por favor, insira um número maior ou igual a zero.")
        

n = solicitar_numero()
fibonacci_linear(n)


