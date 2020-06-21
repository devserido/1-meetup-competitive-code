totalNumeros = int(input())
numeros = []

for i in range(totalNumeros):
    index = int(input())
    numeros.append(index)

cadastrados = {}

def fibo(n):
    if n == 1 or n == 0:
        return n

    try:
        return cadastrados[n]

    except:
        cadastrados[n] = fibo(n-1) + fibo(n-2)
        return cadastrados[n]

for index in numeros:
    print('Fib(' + str(index) + ') = ' + str(fibo(index)))


'''
#Essa segunda parte também funciona, mas sem o aperfeiçoamento

totalNumeros = int(input())
numeros = []

for i in range(totalNumeros):
    index = int(input())
    numeros.append(index)


for index in numeros:
    atual = 0
    proximo = 1
    auxiliar = 0

    for j in range(index):
        auxiliar = atual + proximo
        atual = proximo
        proximo = auxiliar
    print('Fib(' + str(index) + ') = ' + str(atual))
'''
