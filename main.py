import cv2
import os
from cvzone.HandTrackingModule import HandDetector # Módulo de detección de manos


cap = cv2.VideoCapture(0) # Capturar webcam
cap.set(3, 640) # Dimensiones - Pixeles eje x
cap.set(4, 480) # Dimensiones - Píxeles eje y

imgFondo = cv2.imread("Recursos/fondo.png") # Leer la imagen base de nuestra interfaz gráfica

directorio_Opciones = "Recursos/Opciones" # Directorio "Opciones"
listaRutas_Opciones = os.listdir(directorio_Opciones) # Almacenar el nombre de todos los archivos del directorio seleccionado
lista_Opciones = []
# Leer cada uno de los archivos almacenados (Imágenes)
for imgOpcion in listaRutas_Opciones: 
    lista_Opciones.append(cv2.imread(directorio_Opciones + "/" + imgOpcion)) 


directorio_Iconos = "Recursos/Iconos" # Directorio "Iconos"
listaRutas_Iconos = os.listdir(directorio_Iconos) # Almacenar el nombre de todos los archivos del directorio seleccionado
lista_Iconos = []
# Leer cada uno de los archivos almacenados (Imágenes)
for imgIcono in listaRutas_Iconos:
    lista_Iconos.append(cv2.imread(directorio_Iconos + "/" + imgIcono))

# ------------------------------------------------- VARIABLES -------------------------------------------------------------------

opcionActiva = 0 # Determina la imagen de opción que se muestra en pantalla
memoriaSelecciones = [-1, -1, -1] # Almacena las seleccion de cada pantalla de Opción (Recipiente - Tamaño - Sabor) 
selección = -1 # -1 == Selección nula
cont = 0
cooldown = 0
posicionElipse = [0, (1155, 250),(980, 505), (1168,168), (971,367), (1168,575)] # Posición en la que se mostrará la elipse (Centro de la circunferencia)
detector = HandDetector(detectionCon=0.8, maxHands=1) # Índice de confianza (0-1) y número máximo de manos para detectar simultáneamente

# ------------------------------------------------- VARIABLES -------------------------------------------------------------------

while True: # Bucle infinito para mostrar imágenes una detrás de otra (Vídeo)
    success, img = cap.read() 

    hands, img = detector.findHands(img) # Método que detecta las manos y sus puntos de referencia
    
    # Interfaz gráfica
    imgFondo[141:141+480, 49:49+640] = img # Ajustando la webcam a la imagen de fondo
    imgFondo[0:720, 849:1280] = lista_Opciones[opcionActiva] # Ajustando la imagen de opción correspondiente a la imagen de fondo

    # Dependiendo del número de dedos elije entre las diferentes opciones y muestra la imagen "Opción" correspondiente (Siguiente selección)
    if hands and cooldown == 0 and opcionActiva < 4:
            hand1 = hands[0]
            fingers1 = detector.fingersUp(hand1)
            print(fingers1)

            if opcionActiva == 0: # Primera imagen "Opción" (TARRINA, selección 1 - CONO, selección 2)

                if fingers1 == [0,1,0,0,0]: # Dedo índice levantado (Signo "1" - Selección 1)
                    if selección != 1:
                        cont = 1
                    selección = 1

                elif fingers1 == [0,1,1,0,0]: # Dedos índice y corazón levantados (Signo "2" - Selección 2)
                    if selección != 2:
                        cont = 1
                    selección = 2
                else:
                    cont = 0
                    selección = -1 # Gesto con la mano diferente a los signos 1 o 2, ninguna opción seleccionada

                if cont > 0: # El contador indica durante cuanto tiempo se ha estado haciendo el gesto 1 o 2 - Tiempo de comprobación
                        if cont < 365/5: # 365 (frames mostrados) entre 5 (VARIABLE que disminuye el tiempo de comprobación)
                            cont += 1 # Mientras el número de frames sea inferior a 365/5 sigue contando los frames

                            # -------------------------- ELIPSE ------------------------------------------------------------------
                            # Valores: (Imagen donde se mostrará la elipse, Posición en píxeles del centro de la circunferencia (varía segun la imagen "Opción"), Radio de la elipse (x,y), Ángulo inicial, Ángulo final, Valor de la elipse, Color (RGB), Grosor)
                            cv2.ellipse(imgFondo, posicionElipse[selección], (95,95), 95 , 0,cont*5, (0,255,0), 20)
                            # Utiliza como valor el número de frames consecutivos en los que se detecta el signo correspondiente
                            # ----------------------------------------------------------------------------------------------------

                        else: # Cuando el contador supera el número de frames establecido (365/5)...
                            # ...elige la opción seleccionada y cambia a la pantalla correspondiente,...
                            if selección == 1:
                                opcionActiva += 1
                            if selección == 2: 
                                opcionActiva += 2
                            # ... almacena la selección en la memoria...
                            memoriaSelecciones[0] = selección
                            # ...y resetea todos los parámetros.
                            cont = 0
                            selección = -1
                            cooldown = 1

            else: # Hace lo mismo que hemos visto antes con el resto de pantallas pero ahora con una tercera opción
                if fingers1 == [0,1,0,0,0]:
                    if selección != 1:
                        cont = 1
                    selección = 1

                elif fingers1 == [0,1,1,0,0]:
                    if selección != 2:
                        cont = 1
                    selección = 2
                elif fingers1 == [0,1,1,1,0]: # Dedos índice, corazón y anular levantados (Signo "3" - Selección 3)
                    if selección != 3:
                        cont = 1
                    selección = 3
                else:
                    cont = 0
                    selección = -1

                if cont > 0:
                        if cont < 365/5:
                            cont += 1
                            print(cont)
                            cv2.ellipse(imgFondo, posicionElipse[selección+2], (75,75), 95 , 0,cont*5, (0,255,0), 15)
                        else:
                            print("Opcion " + str(selección) + " seleccionada")
                            if opcionActiva == 1:
                                opcionActiva += 2
                                memoriaSelecciones[1] = selección + 2
                            elif opcionActiva == 2:
                                memoriaSelecciones[1] = selección + 5
                                opcionActiva +=1
                            else:
                                memoriaSelecciones[2] = selección + 8
                                opcionActiva += 1
        
                            cont = 0
                            selección = -1
                            cooldown = 1

    # Tiempo de reposo entre selección y selección (40 frames)
    if cooldown > 0:
        cooldown += 1
        if cooldown > 40: 
            cooldown = 0

    # Mostrar el icono con la selección correspondiente
    if memoriaSelecciones[0] != -1: # Si la primera selección es diferente a "-1" (Selección nula)...
        # ...muestra el primer icono - Primera selección "Recipiente: (1.Tarrina - 2.Cono)""
        imgFondo[638:720, 146:228] = lista_Iconos[memoriaSelecciones[0] - 1]
    
    if memoriaSelecciones[1] != -1: # Si la segunda selección es diferente a "-1" (Selección nula)...
        # ...muestra el segundo icono - Segunda selección "Tamaño: (1.Pequeño - 2.Mediano - 3.Grande)"
        imgFondo[638:720, 328:410] = lista_Iconos[memoriaSelecciones[1] - 1]

    if memoriaSelecciones[2] != -1: # Si la tercera selección es diferente a "-1" (Selección nula)...
        # ...muestra el tercer icono - Tercera selección "Sabor: (1.Fresa - 2.Chocolate - 3.Limón)"
        imgFondo[638:720, 518:600] = lista_Iconos[memoriaSelecciones[2] - 1]


    # Mostrar proceso
    cv2.imshow('Fondo', imgFondo)
    cv2.waitKey(1) # 1 milisegundo entre imagen y imagen
