coeficientes = input()
coefsplit = coeficientes.split(" ")
a = float(coefsplit[0])
b = float(coefsplit[1])
c = float(coefsplit[2])
if (a == 0) or ((b**2)-(4*a*c)<0):
    print("Impossivel calcular")
else:
    R1 = (-b+((b**2)-(4*a*c))**0.5)/(2*a)
    R2 = (-b-((b**2)-(4*a*c))**0.5)/(2*a)
    print("R1 = %.5f" % (R1))
    print("R2 = %.5f" % (R2))
