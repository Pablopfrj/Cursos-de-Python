times = 'Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória','Curitiba','Avaí','Ponte preta','Atlético-GO'

print("*-"*30)
print(f'Lista de times do brasileirão {times}')
print("*-"*30)
print(f'Os 5 primeiros são {times[:5]}')
print("*-"*30)
print(f'Os 4 ultimos do brasileirão são: {times[-4:]}')
print("*-"*30)
print(f'Times em ordem alfábetica: {sorted(times)}')
print("*-"*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição.')
