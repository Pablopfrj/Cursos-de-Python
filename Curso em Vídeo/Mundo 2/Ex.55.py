maior=0
menor=0
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior > peso:
            maior = peso
        if menor < peso:
            menor = peso
print('O menor peso é {}Kg e o maior é {} Kg. '.format(maior,menor))

