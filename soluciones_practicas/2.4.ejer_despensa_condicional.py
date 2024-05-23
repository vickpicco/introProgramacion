# Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
# Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
# Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
# La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

precio_leche = 1000
cantidad_leches = int(input('Ingresa la cantidad de leches: '))
jubilado = input('Es jubilado? (S/N)')

total = precio_leche * cantidad_leches

if cantidad_leches >= 12 and cantidad_leches <= 24:
    if jubilado == 'S':
        total = total - total * 0.2
    else: 
        total = total - total * 0.1

if cantidad_leches > 24:
    if jubilado == 'S':
        total = total - total * 0.25
    else: 
        total = total - total * 0.15

print('El total es: $', total)