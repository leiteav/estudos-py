print('*** Verificação de números primos ***')

div = 0
numdig = int(input('Entre com um nº inteiro: '))

for i in range(1, numdig + 1):
    resto = numdig % i
    if resto == 0:
        div = div + 1

if div == 2:
    print('{} É um número primo.'.format(numdig))
else:
    print('{} Não é um número primo.'.format(numdig))