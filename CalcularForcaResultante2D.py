f1 = ""
f2 = ""
f1 = input("Digite os valores de f1, x1, y1, z1: ").split()
f2 = input("Digite os valores de f2, x2, y2, z2: ").split()
for i in range(3):
    f1[i] = float(f1[i])
    f2[i] = float(f2[i])
fres = [f1[0]-f2[0], f1[1]-f2[1], f1[2]-f2[2]]
print ("Forca resultante em X: "+str(fres[0])+"\n")
print ("Forca resultante em Y: "+str(fres[1])+"\n")
print ("Forca resultante em Z: "+str(fres[2])+"\n")
