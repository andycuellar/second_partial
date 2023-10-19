temperatura=float(input("Ingresa la temperatura del paciente en grados Celsius:"))
dias=input("Ingresa la cantidad de día que el paciente ha estado enfermo:")
sintomas=input("Ingresa una lista de síntomas que el paciente presenta:")
if temperatura <=36.5:
  print("No tiene fiebre")
elif  temperatura>= 36.5 or 36.6 or 36.7 or 36.8 or 36.9 or 37 or 37.1 or 37.2 or 37.3 or 37.4 or 37.5 or 37.6 or 37.7 or 37.8 or 37.9 or 38:
  print("Fiebre baja")
elif temperatura >=38:
  print("Fiebre alta")
  
if dias>='7' and sintomas=='tos crónica':
  print("Enfermedad crónica")

if temperatura >= 36 or 36.1 or 36.2 or 36.3 or 36.4 or 36.5 or 36.6 and sintomas=='tos':
  print("Infección respiratoria leve")
elif temperatura>=36.6 or 36.7 or 36.8 or 36.9 or 37 or 37.1 or 37.2 or 37.3 or 37.4 or 37.5 or 37.6 or 37.7 or 37.8 or 37.9 or 38 and sintomas=='tos'or'dolor de garganta':
  print("Infección respiratoria media")
else:
  print("Infección respiratoria grave")
