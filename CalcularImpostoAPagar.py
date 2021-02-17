salario = float(input())
tributo = 0.00
if salario <= 2000:
    print("Isento")
elif 2000.01 <= salario <= 3000.00:
    tributavel1 = (salario-2000)*0.08
    print("R$ %.2f" % (tributavel1))
elif 3000.01 <= salario <= 4500.00:
    salario -= 2000
    tributo = 1000*0.08
    salario -= 1000
    tributo += salario*0.18
    print("R$ %.2f" % (tributo))
else:
    salario -= 2000
    tributo = 1000 * 0.08
    salario -= 1000
    tributo += (1500 * 0.18)
    salario -= 1500
    tributo += (salario * 0.28)
    print("R$ %.2f" % (tributo))
