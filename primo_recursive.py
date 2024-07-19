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

def obter_primos_recursivo(n):
    def encontrar_primos_atual(atual):
        if atual < 2:
            return []
        primos = encontrar_primos_atual(atual - 1)
        if verificar_primo_recursivo(atual):
            primos.append(atual)
        return primos
    
    if n <= 1:
        return "Insira um número maior que 1"
    
    return encontrar_primos_atual(n)

n = int(input('Digite um número: '))
print(obter_primos_recursivo(n))
