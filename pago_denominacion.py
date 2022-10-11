total = int(input("ingrese el total de la venta"))
pago = int(input("ingrese el valor pagado por el comprador"))

if pago < total:
  print("el valor pagado no es suficiente")
else:
    cambio = pago - total

print("el cambio es ", cambio)

denominaciones = [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]

for denominacion in denominaciones:
  cantidad = cambio // denominacion
  cambio = cambio % denominacion
  if cantidad > 0:
    print(cantidad,"de",denominacion)