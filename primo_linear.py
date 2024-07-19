def verifica_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obter_primos(n):
    if n <= 1:
        return "Insira um número maior que 1."
    
    primos = []
    for num in range(2, n + 1):
        if verifica_primo(num):
            primos.append(num)
    return primos

n = int(input('Digite um número: '))
print(obter_primos(n))
