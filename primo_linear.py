def verifica_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def obter_primos(n):
    primos = []
    for num in range(2, n + 1):
        if verifica_primo(num):
            primos.append(num)
    return primos

def solicitar_numero():
    while True:
        n = int(input('Digite um número maior que um: '))
        if n > 1:
            return n
        else:
            print("Por favor, insira um número maior que um.")
        

n = solicitar_numero()
primos = obter_primos(n)
print(primos)

