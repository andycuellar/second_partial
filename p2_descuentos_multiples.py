https://replit.com/@AndreaCuellar2/P2-A6-Ej-Tipo-Examen-1?v=1

#Compra con descuentos múltiples
precio=float(input("Hola, buen día! Por favor ingresa el precio del producto:"))
unidades=float(input("Ingresa la cantidad de unidades:"))
categoria=input("Ahora ingresa la categoría: A, B o C: ")
if categoria=='A':
  precio=int(precio)-int(precio)*.10
  print("Tu precio con descuento es", precio)
elif categoria=='B':
  precio=int(precio)-int(precio)*.05
  print("Tu precio con descuento es", precio)
elif categoria=='C':
  precio=int(precio)-int(precio)*.02
  print("Tu precio con descuento es", precio)
if unidades>=10:
  extra=0.5
  print("Obtienes un descuento adicional del 5%", int(precio)-int(precio)*.05)
