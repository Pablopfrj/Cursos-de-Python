num = (int(input('Digite um valor: ')),
    int(input('Digite um outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor : ')))
print(f"Você digitou os valores: {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes ")
if 3 in num:
    print(f"O valor 3 apareceu na posiçao {num.index(3)+1} ")
else:
    print('Não tem valor 3.')
print("Os valores pares são ", end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')

