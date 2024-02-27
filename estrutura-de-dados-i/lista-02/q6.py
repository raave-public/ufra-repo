# 6. Mostre-me as seguintes listas, derivadas de : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 	1. Intervalo de 1 a 9.
# 	2. Intervalo de 8 a 13
# 	3. Números Pares
# 	4. Números Ímpares
# 	5. Todos os multiplos 2,3 e 4
# 	6. Lista Reversa

# Lista original
lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Intervalo de 1 a 9
intervalo_1_9 = lista_original[1:10]
print("Intervalo de 1 a 9:", intervalo_1_9)

# Intervalo de 8 a 13
intervalo_8_13 = lista_original[8:14]
print("Intervalo de 8 a 13:", intervalo_8_13)

# Números Pares
numeros_pares = [numero for numero in lista_original if numero % 2 == 0]
print("Números Pares:", numeros_pares)

# Números Ímpares
numeros_impares = [numero for numero in lista_original if numero % 2 != 0]
print("Números Ímpares:", numeros_impares)

# Todos os múltiplos de 2, 3 e 4
multiplos_2_3_4 = [numero for numero in lista_original if numero % 2 == 0 or numero % 3 == 0 or numero % 4 == 0]
print("Todos os múltiplos de 2, 3 e 4:", multiplos_2_3_4)

# Lista Reversa
lista_reversa = lista_original[::-1]
print("Lista Reversa:", lista_reversa)
