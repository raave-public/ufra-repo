# 5. Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas.

#Inicializando a lista de 20 números inteiros
numeros_inteiros = [5, 12, 7, 8, 23, 16, 9, 4, 11, 18, 25, 6, 13, 10, 3, 19, 2, 14, 21, 17]

# Inicializando as listas para armazenar os números pares e ímpares
numeros_pares = []
numeros_impares = []

# Separando os números pares e ímpares
for numero in numeros_inteiros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Imprimindo as listas de números pares e ímpares
print("Números Pares:", numeros_pares)
print("Números Ímpares:", numeros_impares)
