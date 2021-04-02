num = ('zero' , 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
pedir_num = int(input('Digite um número entre 0 a 20: '))
resp = ''

while True:
    while pedir_num not in range(0, 21):
        pedir_num = int(input('Tente novamente. Digite um número de 0 a 20: '))
        print(f'Você digitou o número {num[pedir_num]}.')
        resp = str(input('Quer continuar?[S/N] ')).upper()
        while resp not in 'SN':
            resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
        if resp == 'N':
            break
print('Fim')



