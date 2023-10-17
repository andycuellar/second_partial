https://replit.com/join/vccwajyypc-andreacuellar2

ruedas=input("Ingresa el número de ruedas del vehículo:")
combustible=input("Ingresa el tipo de combustible que utiliza el vehículo:")
emisiones=float(input("Ingresa la cantidad de emisiones de C02 que genera el vehículo:"))
if ruedas>='4' and       combustible=='gasolina'or'Gasolina' and emisiones>=150:
  print("Su vehículo es grande y contaminante")
elif ruedas=='4'and combustible=='eléctrico'or'Eléctrico':
  print("Su vehículo es eléctrico")
if combustible=='Gasolina'or'gasolina':
  print("Su vehículo es de gasolina")
else:
  print("Su vehículo es de diésel")

  
