palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end=' ')
    for vogais in i:
        if vogais in 'aeiou':
            print(f'{vogais}', end=' ') 
    
    