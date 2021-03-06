import math

A1 = float(input('Digite o valor de A: '))

B1 = float(input('Digite o valor de B: '))

C1 = float(input('Digite o valor de C: '))

Delta = float((B1**2 - 4*A1*C1))

if (Delta<0):

    print('As raízes dessa equaçao não existem.')

else :

    if (Delta == 0) :
       
        Ru = -B1/2*A1 + 0

        print('A raiz dessa equação é : ',Ru) 

    else :

        if (Delta > 0):

            R1 = (- B1 + math.sqrt(Delta))/2*A1

            R2 = (- B1 - math.sqrt(Delta))/2*A1

            print('A raizes são :', R1 ,'e',R2)



