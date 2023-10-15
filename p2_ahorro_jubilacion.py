https://replit.com/@AndreaCuellar2/P2-A6-Ej-Tipo-Examen-2?v=1

edad=float(input("Ingrese su edad actual:"))
jubilacion=float(input("Ingrese la edad a la que planea jubilarse:"))
cantidad=float(input("Ingrese la cantidad deseada para su jubilación:"))
r=0.25/12
n=(jubilacion-edad)*12
t=jubilacion-edad
numero=jubilacion*r
funcion=((1+r)**n-1*(1+r)**(-t))
pmt=numero/funcion
print("El pago mensual para la jubilación es de", pmt)
