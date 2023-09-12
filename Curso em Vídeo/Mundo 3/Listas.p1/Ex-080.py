nums = []
for pos,c in enumerate(range(1,5)):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > nums[-1]:
        nums.append(valor)
        print('Adicionado no final da lista...')
    else:
        pos=0
        while pos < len(nums):
            if valor <= nums[pos]:
                nums.insert(pos,c)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print(f'Os valores digitados são em ordem {nums}')
    
    






