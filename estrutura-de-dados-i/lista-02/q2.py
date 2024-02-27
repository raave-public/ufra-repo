# 2. Explique a diferença entre *listas* e *tuplas* e mostre essa diferença usando um código básico em Python.

# Lista
lista = [1, 2, 3]
print("Lista original:", lista)

# Alterando um elemento da lista
lista[0] = 4
print("Lista após modificação:", lista)

# Adicionando um novo elemento à lista
lista.append(5)
print("Lista após adição de um novo elemento:", lista)

# Removendo um elemento da lista
del lista[1]
print("Lista após remoção de um elemento:", lista)

# Tupla
tupla = (1, 2, 3)
print("Tupla original:", tupla)

# Tentativa de alterar um elemento da tupla (gerará um erro)
# tupla[0] = 4  # Descomente esta linha para ver o erro

# Tentativa de adicionar um novo elemento à tupla (gerará um erro)
# tupla.append(4)  # Descomente esta linha para ver o erro

# Tentativa de remover um elemento da tupla (gerará um erro)
# del tupla[1]  # Descomente esta linha para ver o erro