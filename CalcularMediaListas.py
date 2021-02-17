notas = []
escolha = True
while(escolha==True):
    notas.append(float(input("Digite a nota do aluno: ")))
    escolharec = input("Deseja continuar? ")
    if escolharec == 'n' or escolharec == 'N':
        escolha = False
print(notas)
houve10 = 10 in notas
if houve10 == True:
    print("Tiraram 10...")
tamanho = len(notas)
print(str(tamanho) + " notas adicionadas")
soma = 0
for i in range(tamanho):
    soma = notas[i] + soma
print("A media eh "+ str(soma/tamanho))
