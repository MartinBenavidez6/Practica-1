## ejercicio 7
lista = []
for i in range(4):
    numero = int(input("Ingresar número entero: "))
    lista.append(numero)
cadena_final = "-".join(str(num) for num in lista if num % 3 != 0)
print("Cadena final sin múltiplos de 3:", cadena_final)