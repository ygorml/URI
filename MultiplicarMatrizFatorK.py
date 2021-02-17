matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
k = 5
for linha in range(3):
    for coluna in range(3):
        valor = int(input("Digite o valor do elemento matriz["+str(linha)+"]["+str(coluna)+"]: "))
        matriz[linha][coluna] = valor
print("ANTES: ")
print(matriz)
for linha in range(3):
    for coluna in range(3):
        if linha == coluna:
            matriz[linha][coluna] = matriz[linha][coluna] * k
print("DEPOIS: ")
print(matriz)
