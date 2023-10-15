https://replit.com/@AndreaCuellar2/P2-A6-Ej-Tipo-Examen-7?v=1

millas=float(input("Ingresa la distancia que recorres en millas:"))
millasxgalon=float(input("Ingresa el rendimiento de millas por galón:"))
precio=float(input("Ingresa el precio actual de la gasolina:"))
dias=input("¿Cuántos días vas a viajar?:")
costo=(millas/millasxgalon)*precio*int(dias)
print("El precio por viajar esa distancia es de", costo)
