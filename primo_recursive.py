def verificar_primo_recursivo(num, div=None):
    if num < 2:
        return False
    if div is None:
        div = num - 1
    if div == 1:
        return True
    if num % div == 0:
        return False
    return verificar_primo_recursivo(num, div - 1)

def encontrar_primos(numero):
        if numero < 2:
            return []
        primos = encontrar_primos(numero - 1)
        if verificar_primo_recursivo(numero):
            primos.append(numero)
        return primos

def solicitar_numero():
    while True:
        n = int(input('Digite um número maior que um: '))
        if n > 1:
            return n
        else:
            print("Por favor, insira um número maior que um.")
        

n = solicitar_numero()
primos = encontrar_primos(n)
print(primos)

