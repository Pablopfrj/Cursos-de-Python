x = input('Digite o primeiro número : ')
y = input('Digite o segundo número  : ')

if x > y:
    print('\033[30mO \033[33mprimeiro \033[37mvalor é maior !!! ')
elif y > x:
    print('O \033[33msegundo \033[37mvalor é maior !!! ')
elif x == y:
    print('\033[31mNão \033[30mexiste valor maior,os dois são \033[33miguais \033[30m!!!')