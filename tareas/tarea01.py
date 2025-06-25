
categoria = int(input("Ingrese la categoría del trabajador (1 a 4): "))
sueldo = float(input("Ingrese el sueldo actual del trabajador: "))

if categoria == 1:
    aumento = sueldo * 0.20
elif categoria == 2:
    aumento = sueldo * 0.15
elif categoria == 3:
    aumento = sueldo * 0.10
elif categoria == 4:
    aumento = sueldo * 0.05
else:
    aumento = 0

nuevo_sueldo = sueldo + aumento

if categoria >= 1 and categoria <= 4:
    print("Categoría:", categoria)
    print("Nuevo sueldo:", nuevo_sueldo)
else:
    print("Categoría inválida. Sueldo:", sueldo)
