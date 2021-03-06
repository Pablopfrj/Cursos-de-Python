soma = int(input('digite um numero inteiro: '))
resto = 0
while soma!=0:

    resto = (soma % 10) + resto
    
    soma = (soma) // 10

print(resto)