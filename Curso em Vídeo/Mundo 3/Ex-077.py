palavras_vogais = "aprender",'programar','linguagem','python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar','mercado','programador', 'futuro'

for pos in palavras_vogais:
    print(f'\nNa palavra {pos.upper()} temos ', end= '')
    for vog in pos:
        if vog.lower() in 'aeiou':
            print(vog, end=' ')