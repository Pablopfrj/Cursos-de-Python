#INCOMPLETO E ERRADO FÉ COM FÉ

N_original = int(input("Digite o número: "))

N=0
A=0
B=0
while N_original>0 and N_original!= 0 :
    A = N_original % 10 

    N= N_original//10
    
    B= N % 10

if A != B :
    print('sao diferentes')
else:
    print  ('iguais')