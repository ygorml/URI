fib = [0, 1]
termos = int(input("Digite o número de termos a serem calculados: "))
for i in range(termos+1):
    if i>1:
        fib.append(fib[i-1]+fib[i-2])
for i in range(termos+1):
    fib[i] = str(fib[i])
print(", ".join(fib))