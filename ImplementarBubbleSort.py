entrada = input()
valores = entrada.split(" ")
original = []
for i in range(0,len(valores)):
    original.append(valores[i])
for i in range(0,len(valores)):
    valores[i] = int(valores[i])
    original[i] = int(original[i])
for j in range(0,len(valores)):
    for i in range(0,len(valores)-1):
        if valores[i] > valores[i+1]:
            aux = valores[i+1]
            valores[i+1] = valores[i]
            valores[i] = aux
for i in valores:
    print(i)
print("")
for i in original:
    print(i)