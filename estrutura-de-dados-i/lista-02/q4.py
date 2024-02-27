# 4. Faça um programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

def mostrar_inverso(lista):
    inverso = lista[::-1]
    print("Lista na ordem inversa:")
    for numero in inverso:
        print(numero)

# Função para ler uma lista de 10 números reais
def ler_lista():
    lista = []
    print("Digite 10 números reais:")
    for _ in range(10):
        numero = float(input())
        lista.append(numero)
    return lista

# Lendo a lista de números reais
# numeros = ler_lista()

# # Chamando a função para mostrar os números na ordem inversa
# mostrar_inverso(numeros)

numeros_reais = [3.14, 2.718, 1.618, 4.669, 1.414, 2.236, 2.302, 2.718, 3.141, 1.732]
mostrar_inverso(numeros_reais)