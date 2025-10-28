def promedio_notas(notas, cantidad_notas):
    promedio = sum(notas)/cantidad_notas
    return promedio


cantidad_notas = int(input("Cantidad de notas:\n"))
notas = []

for i in range(1, cantidad_notas + 1):
    while True:
        nota = float(input(f"Ingrese {i}° nota:\n"))
        if nota < 1 or nota > 7:
            print("Ingrese nota válida")
        else:
            break
    notas.append(nota)
promedio = round(promedio_notas(notas, cantidad_notas), 1)
    
print(f"El promedio de notas es: {promedio}")
