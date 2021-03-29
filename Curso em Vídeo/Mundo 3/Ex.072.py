num = ('zero' , 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
pedir_num = int(input('Digite um número de 0 a 20: '))
while pedir_num not in range(0,21):
    pedir_num = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número {num[pedir_num]}.')
