resp = 'S'
cont = 0
num = 'Zero','Um', 'Dois', 'Três' , 'Quatro' , 'Cinco' , 'Seis' , 'Sete' , 'Oito' , 'Nove', 'Dez','Onze','Doze','Treze','Catorze','Quinze', 'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'


while resp == 'S':
    if 0 <= cont <= 20:
        cont = int(input('Digite um número de 0 a 20: '))
        print(f'Vocé digitou o número {num[cont]}')
        resp = str(input('Deseja continuar ? [S/N]  ')).upper()[0].strip()
        if resp in 'Nn':
            print('Programa encerrado')
    else: 
        cont = int(input('Tente Novamente.Digite um número de 0 a 20: ', end=''))
    
         

