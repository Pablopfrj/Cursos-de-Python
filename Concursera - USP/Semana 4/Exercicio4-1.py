A = int(input("Digite o valor de N: "))

if A == 0:
    print(1)
else:
    if  A == 2 :
        print(2)
    else:
        while A>2 :
            A = A**(A-1)
            print(A)