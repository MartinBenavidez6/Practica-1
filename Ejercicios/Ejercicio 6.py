## ejercicio 6
numeros = [1,2,3,4,5,6,7,8,9,10]
impar = []
par = []
for numero in numeros:
    if numero % 2 != 0:
        impar.append(numero)
    else:
        par.append(numero)
print(impar)
print(par)