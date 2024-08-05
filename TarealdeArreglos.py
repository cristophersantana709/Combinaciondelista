cantidad = int(input("¿Cuántas temperaturas desea ingresar? "))
temperatura = []
for i in range(cantidad):
    temp = float(input(f"Ingresa la temperatura: #{i + 1} "))
    temperatura.append(temp)
media = sum(temperatura) / cantidad
CSI = sum(1 for temp in temperatura if temp >= media)
print("La media es:" , media)
print("Total de temperaturas >= a la media:" , CSI)