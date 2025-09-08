import numpy as np

print("Versão NumPy", np.__version__)

# Array: "lista" n-dimensional. É bem parecido com a lista, porém traz diversas novas funcionalidades matemáticas com mais rapidez que o python usual.

array_1 = np.array([1,2,3])
array_2 = np.array([[1,2,3], [4,5,6]]) # O Array só aceita uma lista. Por conta disso, para fazer "mais de uma", colocaremos uma lista dentro de outra maior.

print("Array 1:", array_1)
print("Array 2:\n", array_2)

print("="*40)

print("Propriedades dos NDArrays")
print("Formato (shape)") # Mostra o número de listas e a quantidade de objetos dentro de cada uma. As listas devem ter a mesma quantidade de objetos.
print("1D", array_1.shape) # (3, ) - São 3 elementos apenas, sem lista. Por isso só aparece o "3".
print("2D", array_2.shape) # (2,3) - São 2 listas com 3 elementos cada.

print("Tipo dos Dados (dtype)")
print("1D", array_1.dtype)
print("2D", array_2.dtype)

print("Número de dimensões (ndim)")
print("1D", array_1.ndim)
print("2D", array_2.ndim)

print("="*40)

print("Criação de NDArrays")
print("Zeros:\n", np.zeros([2,3])) # Printa uma matriz composta somente de "0" com o shape que você indicar.
print("Uns:\n", np.ones([2,3])) # OBS: retornam floats, ou seja, com valor "decimal". Exemplo: 1.0
print("Cheia:\n", np.full((5,5), 42)) # Retorna uma matriz 5x5 cheia de valores 42
print("ARange:\n", np.arange(0,10,2)) # Retorna uma matriz que pega os valores de 0 a 10, de 2 em 2.
print("Linspace:\n", np.linspace(0,1,5)) # Retorna uma matriz que pega os valores de 0 a 1, divididos em 5 partes.
print("Random:\n", np.random.rand(2,2)) # Retorna uma matriz 2x2 com valores aleatórios de 0 a 1

matriz = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(matriz)

print("\nElemento da linha 1, coluna 2:", matriz[1,2]) # Lembre-se: funciona como lista, então linhas e colunas são 0,1,2.
print("\nPrimeira linha:", matriz[0])
print("\nSegunda coluna", matriz[:,1])
print("\nÚltima linha:", matriz[-1])
print("\nÚltima coluna:", matriz[:,-1])
print("\nSubmatriz (linhas: 0-1, colunas: 1-2):\n", matriz[0:2, 1:3]) # O "slice (:)" funciona como range, não pegando o último elemento.

print("="*40)

print("Operações em NDArrays")
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

print("Soma elemento a elemento:\n", x + y)
print("Multiplicação elemento a elemento:\n", x * y)
print("Prodruto matricial (dot product):\n", x @ y)
print("Transposta de X:\n", x.T)
print("Soma total dos elementos:\n", np.sum(x))
print("Soma por linhas de X:\n", np.sum(x, axis=0))
print("Soma por colunas de X:\n", np.sum(x, axis=1))

print("="*40)
print("Estatística em NDArrays")
data = np.random.randint(1,100,size=10) # Gera uma matriz com 10 elementos no intervalo de 0 - 100
print("NDArray aleatório:", data)
print("Média:", np.mean(data))
print("Desvio Padrão:", np.std(data))
print("Valor máximo", np.max(data))
print("Índice do Valor Máximo:", np.argmax(data))

print("="*40)
print("Indexação Booleana e Condicional em NDArrays")
array_ = np.array([10,15,20,25,30])
print("Array:", array_)
print("Valores maiores que 20:", array_ > 20) # Retorna true/false para cada elemento
print("Valores pares:", array_ % 2 == 0)

print("Valores maiores que 20:", array_[array_ > 20]) # "Filtro booleano": retorna apenas os elementos que passarem pelo filtro
print("Valores pares:", array_[array_ % 2 == 0])