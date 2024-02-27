# 3. Faça um programa que leia uma lista de cinco números inteiros e mostre cada número juntamente com a sua posição na lista.

def mostrar_numeros_e_posicoes(lista):
    for i, numero in enumerate(lista):
        print(f"O número {numero} está na posição {i}.")

# Exemplo de lista de 5 números inteiros
numeros = [10, 20, 30, 40, 50]

# Chamando a função para mostrar os números e suas posições
mostrar_numeros_e_posicoes(numeros)