## ejercicio1
edad = int(input("Ingresar edad actual: "))
if edad > 100:
    print("Ya pasaste los 100 años")
elif edad == 100:
    print("Tenes 100")
elif edad < 100:
    print("Te faltan {}".format(100-edad))
