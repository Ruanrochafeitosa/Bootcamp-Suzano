#Conversão de tipos
# Int para float

x1 = 10
x_float = float(x1)

#Float para int
x2 = 2.0
x_int = int(x2)

#String para int e float
num_str = "12"
num_int = int(num_str)

#Exercícios
#1) Soma de números ímpares entre 1 a 100
num = 100
resultado1 = 0
for i in range(num):
    if i % 2 == 1:
        resultado1 += i

print(f"O resultado da questão 1 é: {resultado1}\n")

#2) Fazer o fatorial de algum número
num2 = 3
resultado2 = 1
for i in range(num2+1):

    if i != 0:
        resultado2 *= i

print(f"O resultado da questão 2 é: {resultado2}\n")

#3) Fazer a média ponderada de notas, com pesos 2, 3 e 5
notas = [2, 5, 9]
media_ponderada = (notas[0]*2 + notas[1]*3 + notas[2]*5) / (2+3+5)
print(f"A resposta da questão 3 é: {media_ponderada}")

#4) Dado um número float arredonde suas casas se a terceira for >= 5

num3 = 3.006
num_str = str(num3)

parte_inteira, parte_decimal = num_str.split('.')

parte_decimal_int = int(parte_decimal[2])
parte_decimal_segunda = int(parte_decimal[1])
if parte_decimal_int >= 5:
    num_str = f"{parte_inteira}.{parte_decimal[0]}{parte_decimal_segunda +1}"

print(f"A resposta da questão 4 é:{num_str}")












