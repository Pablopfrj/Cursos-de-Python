n = cont = soma = maior = menor = 0
conti = ''
while conti != 'N':
    n = float(input('Digite um número: '))
    cont += 1
    soma += n
    conti = str(input('Deseja continuar? [S/N]  ')).upper().strip()
    if conti == 'S':
        if cont == 1:
            maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = soma / cont
print('Você digitou {} números e a média foi {}.'.format(cont, média))
if maior == menor:
    print('Os números são iguais.')
else:
    print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
