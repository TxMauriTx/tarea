
salario = float(input("Ingrese su salario mensual: "))
gastos = float(input("Ingrese sus gastos mensuales: "))
temporada = input("Ingrese la temporada (baja, media, alta): ")

presupuesto = salario - gastos

print("Presupuesto disponible:", presupuesto)

if presupuesto < 400:
    print("No puede viajar. Debe quedarse en casa.")
else:
    if temporada == "baja" and presupuesto >= 1300:
        print("Puede hacer un viaje internacional.")
    elif temporada == "media" and presupuesto >= 800:
        print("Puede hacer un viaje nacional.")
    elif temporada == "alta" and presupuesto >= 400:
        print("Puede hacer un viaje local.")
    else:
        print("El presupuesto no es suficiente para esta temporada.")
