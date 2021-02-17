vetorrec1 = input("Digite os valores do vetor1: ")
vetor1 = vetorrec1.split(" ")
for i in range(0,len(vetor1)):
    vetor1[i] = int(vetor1[i])
vetorrec2 = input("Digite os valores do vetor2: ")
vetor2 = vetorrec2.split(" ")
for i in range(0,len(vetor2)):
    vetor2[i] = int(vetor2[i])
vetorresultante = [vetor1[0]+vetor2[0], vetor1[1]+vetor2[1], vetor1[2]+vetor2[2]]
print(vetorresultante)