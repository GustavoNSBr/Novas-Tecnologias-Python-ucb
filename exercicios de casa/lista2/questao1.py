n = int(input("Digite um numero: "))

soma = 0

for par in range(0,n+1,2):
    soma+=par

print(f"A soma dos pares de 0 até {n} é {soma}")