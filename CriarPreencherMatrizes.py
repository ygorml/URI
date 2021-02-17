# Escrito por YGOR MOREIRA LIMA
# Cria e preenche matrizes de tamanho determinado pelo usuário

linhasa = int(input("Digite o numero de linhas da matriz A: "))
colunasa = int(input("Digite o numero de colunas da matriz A: "))
linhasb = int(input("Digite o numero de linhas da matriz B: "))
colunasb = int(input("Digite o numero de linhas da matriz B: "))
matriza = []
matrizb = []
for i in range(linhasa):
    matriza.append([])
for i in range(linhasb):
    matrizb.append([])
print(matriza)
print(matrizb)
for i in range(linhasa):
    for j in range(colunasa):
        matriza[i].append(0)
for i in range(linhasb):
    for j in range(colunasb):
        matrizb[i].append(0)
print(matriza)
print(matrizb)
for linha in range(linhasa):
    for coluna in range(colunasa):
        valor = int(input("Digite o valor do elemento matrizA["+str(linha)+"]["+str(coluna)+"]: "))
if colunasa == linhasb:
    matrizc = []
    for i in range(linhasa):
        matrizc.append([])
    for i in range(linhasa):
        for j in range(colunasb):
            matrizc[i].append(0)
print(matrizc)
