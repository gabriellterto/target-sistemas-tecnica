string = input("Digite uma string: ")

contagem_a = 0

for char in string:
    if char.lower() == 'a':
        contagem_a += 1

if contagem_a > 0:
    print(f"A letra 'a' aparece {contagem_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
