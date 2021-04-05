n = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num not in range(0,21):
        print('Invalido Tente novamente ', end='')
    else:
        print(f'Você digitou o número {n[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('Fim')



