print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI'.center(30))
print('-' * 30)

usuario = int(input('Digite um número inteiro: '))

a, b = 0, 1
encontrado = False

while a <= usuario:
    if a == usuario:
        encontrado = True
        break
    a, b = b, a + b

if encontrado:
    print(f'O número {usuario} pertence à sequência de Fibonacci.')
else:
    print(f'O número {usuario} não pertence à sequência de Fibonacci.')
