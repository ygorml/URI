vetorrec = input("Digite o vetor de 5 posicoes: ")
vetor = vetorrec.split(" ")
valorprocurado = int(input("Qual o valor desejado? "))
for i in range(0, len(vetor)):
    vetor[i] = int(vetor[i])
indice = vetor.index(valorprocurado)+1
print(str(indice), "posicao")
