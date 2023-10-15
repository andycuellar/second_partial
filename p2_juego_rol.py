personaje= input("Bienvenido al juego de rol! Elije un personaje: guerrero, mago o rey:")
if personaje =='guerrero':
  inicio=input("Elejiste al guerrero, por favor ingresa un número entero del 1 al 10 y veamos si tienes suerte:")
  if inicio>='6':
    print("Tienes suerte, es hora de que inicies el camino. Inicias con 3 vidas")
  elif inicio<='5':
    print("Puedes seguir jugando, pero tu guerrero fue derrotado contra el ogro que cuida la entrada. Pierdes una vida, te quedan 2")
  bosque=input("Te encuentras en un bosque, ¿qué quieres hacer?(ir a la izquierda o a la derecha):")
  if bosque=='izquierda' and inicio>='8':
    encuentro=input("Te encuentras con un ogro, ¿que deseas hacer? huir o sacar espada:")
    if encuentro=='huir':
      print("Te ha alcanzado y te deja sin vida. Pierdes tus vidas por la gravedad de las heridas, fin del juego.")
    elif encuentro=='sacar espada':
      print("Haz derrotado al ogro, logras sobrevivir y ganas el juego")
  if bosque=='izquierda' and inicio<='7':
      print("Que gran suerte! El ogro no te vió y pudiste pasar caminando por el bosque")
  if bosque=='derecha':
      pueblo=input("Terminaste en un pueblo sin saber a donde ir, pides instrucciones y te dirijen a dos caminos ¿Cuál tomas? derecha o izquiera:")
  if pueblo=='derecha':
    print("Te asesinaron unos espectros")
  else:
    print("Llegaste a tu reino, lo lograste!")
if personaje =='mago':
  inicio=input("Elejiste al mago, por favor ingresa un número entero del 1 al 10 y veamos si tienes suerte:")
  if inicio>='6':
    print("Tienes suerte, es hora de que inicies el camino. Inicias con 3 vidas")
  elif inicio<='5':
    print("Puedes seguir jugando, pero tu mago fue derrotado en un combate de magia contra el mago oscuro y tendrás que buscar otra manera de llegar a la torre. Pierdes una vida.")
  bosque=input("Te encuentras en un bosque, ¿qué quieres hacer?(ir a la izquierda o a la derecha):")
  if bosque=='izquierda' and inicio>='8':
    encuentro=input("Te encuentras con el mago oscuro, ¿que deseas hacer? huir o usar un hechizo:")
    if encuentro=='huir':
      print("Te ha alcanzado y te deja sin vida. Pierdes tus vidas por la gravedad de las heridas, fin del juego.")
      if encuentro=='usar hechizo':
        print("Haz derrotado al mago oscuro, logras sobrevivir y ganas el juego")
        if bosque=='derecha':
          pueblo=input("Terminaste en una aldea sin saber a donde ir, pides instrucciones y te dirijen a dos caminos ¿Cuál tomas? derecha o izquiera:")
          if pueblo=='derecha':
            print("Te asesinaron unos esqueletos mágicos")
          else:
            print("Llegaste a tu reino, lo lograste!")
if personaje=='rey':
  inicio=input("Elejiste al rey, por favor ingresa un número entero del 1 al 10 y veamos si tienes suerte:")
  if inicio>='6':
    print("Tienes suerte, es hora de que gobiernes tu reino. Inicias con 3 vidas")
  elif inicio<='5':
    print("Puedes seguir jugando, pero tu rey fue derrotado en un combate con el reino enemigo, mucho murieron y debes de tomar una decisión. Seguir adelante o retroceder por más refuerzos:")
    if inicio=='seguir adelante':
      print("Te encuentras con un grupo de monstruos y te han enfrentado, pierdes vidas por la fuerza de los monstruos.")
    else:
      print("Más hombres se unen a ti y logras sobrevivir, ganas el juego")
