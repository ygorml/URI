fib = [0, 1]
termos = int(input())
for i in range(termos):
    if i>1:
        fib.append(fib[i-1]+fib[i-2])
for i in range(termos):
    fib[i] = str(fib[i])
print(" ".join(fib))