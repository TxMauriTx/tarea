
print("Ingrese las temperaturas de los últimos 3 días:")
t1 = float(input("Día 1: "))
t2 = float(input("Día 2: "))
t3 = float(input("Día 3: "))

promedio_temp = (t1 + t2 + t3) / 3
humedad = float(input("Ingrese la humedad actual (%): "))

if promedio_temp > 30 and humedad < 40:
    litros = 10
    nivel = "Riego alto"
elif promedio_temp > 25 and humedad < 60:
    litros = 5
    nivel = "Riego medio"
else:
    litros = 2
    nivel = "Riego bajo"

print("Promedio de temperatura:", promedio_temp)
print("Humedad actual:", humedad)
print("Nivel de riego:", nivel)
print("Litros de agua a usar:", litros)
