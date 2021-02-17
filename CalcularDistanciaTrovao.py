# Por YGOR MOREIRA LIMA - github.com/ygordev
# Descrição: Calcula a distância do ouvinte ao local de queda de um raio, considerando o tempo transcorrido para ouvir o trovão

tempo = float(input("Digite o tempo transcorrido entre ver o raio e ouvir o trovao: "))
distancia = float((340*tempo)/1000)
print("A distancia em km eh: " +str(distancia)+" km")