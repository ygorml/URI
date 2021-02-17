valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())
par = 0
impar = 0
positivo = 0
negativo = 0
if valor1 % 2 == 0:
    par += 1
else:
    impar += 1
if valor2 % 2 == 0:
    par += 1
else:
    impar += 1
if valor3 % 2 == 0:
    par += 1
else:
    impar += 1
if valor4 % 2 == 0:
    par += 1
else:
    impar += 1
if valor5 % 2 == 0:
    par += 1
else:
    impar += 1
if valor1 > 0:
    positivo += 1
elif valor1 < 0:
    negativo += 1
if valor2 > 0:
    positivo += 1
elif valor2 < 0:
    negativo += 1
if valor3 > 0:
    positivo += 1
elif valor3 < 0:
    negativo += 1
if valor4 > 0:
    positivo += 1
elif valor4 < 0:
    negativo += 1
if valor5 > 0:
    positivo += 1
elif valor5 < 0:
    negativo += 1
print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(positivo) + " valor(es) positivo(s)")
print(str(negativo) + " valor(es) negativo(s)")