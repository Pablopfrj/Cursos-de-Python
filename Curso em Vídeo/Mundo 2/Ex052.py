num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[mO numero foi dividido 2 vezes,logo é PRIMO')
else:
    print('\n\033[mO número foi divido {},logo não é PRIMO'.format(tot))
