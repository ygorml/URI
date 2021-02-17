# por YGOR MOREIRA LIMA - github.com/ygordev
# Descrição: Preenche duas matrizes 2x2 com valores determinados pelo usuário e soma em uma matrizC.

mata = [[0, 0], [0, 0]]
matb = [[0, 0], [0, 0]]
matc = [[0, 0], [0, 0]]
for linha in range(2):
    for coluna in range(2):
        valora = int(input("Digite o valor MatA["+str(linha)+"]["+str(coluna)+"]: "))
        valorb = int(input("Digite o valor MatB["+str(linha)+"]["+str(coluna)+"]: "))
        mata[linha][coluna] = valora
        matb[linha][coluna] = valorb
        matc[linha][coluna] = valora + valorb
print(matc)