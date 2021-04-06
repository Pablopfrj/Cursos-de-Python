from random import randint

num = (randint(1,11),randint(1,11),randint(1,11),randint(1,11),
       randint(1,11),randint(1,11))
print(f'Eu sortei os números {num}')
print(f'O maior número é {max(num)}.')
print(f'O menor numeros é {min(num)}.')