vetorrec = input("Digite 10 valores para verificacao: ")
vetorcompara = vetorrec.split(" ")
tamanho = len(vetorcompara)
comparados = []
for j in range(0,len(vetorcompara)):
    for i in range(0, len(vetorcompara)-1):
        if (vetorcompara[i] == vetorcompara[i+1]) and (not(vetorcompara[i] in comparados)):
            tamanho = tamanho - 1
            comparados.append(vetorcompara[i])
print("Temos " +str(tamanho)+ "numeros diferentes")
