# Por YGOR MOREIRA LIMA 
# Descrição: Calcula a média de um aluno, considerando uma entrada separada por espaços

notas = ""
notas = input("Digite as notas do aluno, separadas por espaços: ").split()
print(notas)
houve10 = 10 in notas
if houve10 == True:
    print("Tirou ao menos uma nota 10...")
tamanho = len(notas)
print(str(tamanho) + " notas adicionadas")
soma = 0
for i in range(tamanho):
    soma = int(notas[i]) + int(soma)
print("A media eh "+ str(soma/tamanho))
