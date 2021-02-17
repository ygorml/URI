# por YGOR MOREIRA LIMA - githbub.com/ygordev
# Descrição: 
# 
# Dada um array "lista", um valor e uma a posição para inserção, será realizado um deslocamento
# dos items do array de forma a abrir espaço para o novo item.

lista = [1, 2, 3, 4]
lista.append(0)
print(lista)
pos = 2
#abre espaço para inserir o novo elemento
for i in range(len(lista)-1, pos-1, -1):
    print(str(i))
    lista[i] = lista[i-1]
    print(lista)
lista[pos] = 10
print(lista)