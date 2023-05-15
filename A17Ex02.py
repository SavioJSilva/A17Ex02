numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero adicionado com sucesso!')
    else:
        print('Esse numero ja foi adicionado, não irei adicionar novamente!')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r in 'Nn':
        break
print('--' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')