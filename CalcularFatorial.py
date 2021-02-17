termos = int(input())
fatorial = 1
if 0<termos<13:
    for i in range(1, termos+1):
        fatorial = fatorial * i
print(str(fatorial))