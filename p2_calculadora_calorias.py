https://replit.com/@AndreaCuellar2/P2-A6-Ej-tipo-Examen-3?v=1

peso=float(input("Ingresa tu peso en kilogramos:"))
duracion=float(input("Ingresa la duración en minutos:"))
actividad=input("Ingresa el tipo de actividad (correr, nadar, caminar, ciclismo, levantar pesas):")
if actividad=='correr':
  calorias=9.8*peso*duracion
  print("La cantidad de calorías quemadas es", calorias)
elif actividad=='nadar':
  calorias=7*peso*duracion/200
  print("La cantidad de calorías quemadas es", calorias)
elif actividad=='ciclismo':
  calorias=6*peso*duracion/200
  print("La cantidad de calorías quemadas es", calorias)
elif actividad=='caminar':
  calorias=2.9*peso*duracion/200
  print("La cantidad de calorías quemadas es", calorias)
elif actividad=='levanta pesas':
  calorias=3*peso*duracion/200
  print("La cantidad de calorías quemadas es", calorias)
