origen=input("Ingresa la unidad de origen (kilómetros, millas, litros, galones, fahrenheit, celsius ):")
destino=input("Ingresa la unidad de destino(kilómetros, millas, litros, galones, fahrenheit, celsius):")
cantidad=float(input("Ingresa la cantidad a convertir:"))
if origen=='fahrenheit' and destino=='celsius':
  conversion=(int(cantidad-32)/1.8)
  print("la temperatura en celsius es",conversion)
elif origen=='celsius' and destino=='fahrenheit':
  conversion=(int(cantidad)*9/5+32)
  print("la temperatura en fahrenheit es",conversion)
elif origen=='kilómetros' and destino=='millas':
  conversion=cantidad*1.60934 
  print("la conversión a kilómetros es",conversion)
elif origen=='millas' and destino=='kilómetros':
  conversion=cantidad/1.60934 
  print("la conversión a kilómetros es",conversion)
elif origen=='litros' and destino=='galones':
  conversion=cantidad/3.78541
  print("la conversión a galones es",conversion)
elif origen=='galones' and destino=='litros':
  conversion=cantidad*3.78541
  print("la conversión a litros es",conversion)
