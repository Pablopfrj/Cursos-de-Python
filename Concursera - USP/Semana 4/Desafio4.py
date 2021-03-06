n = int(input("Digite uma sequência de números: "))

soma = 0

u=0

while n > 0:
    u = n % 10
    n = n // 10

soma = u + soma

print('A soma dos digitos é: ',soma)