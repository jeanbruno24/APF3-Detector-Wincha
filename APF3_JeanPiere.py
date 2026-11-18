Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# ============================================================
# APF3 - Detector de WINCHA con Haar Cascade
# Autor: [Tu nombre y apellido]
# Curso: [Nombre del curso] - UTP
# Descripcion: detecta una wincha (cinta metrica) en tiempo real
#              usando OpenCV y un modelo Haar Cascade entrenado
#              con Cascade Trainer GUI.
# Teclas: ESC = salir
# ============================================================
import cv2  # OpenCV: manejo de camara, imagenes y deteccion

# --- Camara ---
# DroidCam por WiFi (cambia la IP por la que muestre la app del celular)
cap = cv2.VideoCapture("http://10.113.163.222:4747/video")
# Alternativa: webcam de la laptop
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# --- Modelo ---
# Carga el modelo entrenado (debe estar en la misma carpeta que este archivo)
WinchaClassif = cv2.CascadeClassifier('cascade.xml')
if WinchaClassif.empty():
    raise SystemExit('No se pudo cargar cascade.xml (esta en la misma carpeta?)')

# --- Parametros de deteccion (se ajustan probando) ---
# scaleFactor: cuanto se reduce la imagen en cada paso de busqueda
# minNeighbors: sube este valor si detecta cosas que NO son la wincha;
#               bajalo si no detecta la wincha
# minSize: tamano minimo (ancho, alto) del objeto a detectar
scaleFactor = 1.3
minNeighbors = 10
... minSize = (70, 70)
... 
... fallos = 0  # cuenta las lecturas fallidas seguidas de la camara
... 
... while True:
...     # Lee un cuadro de la camara
...     ret, frame = cap.read()
...     if not ret:
...         fallos += 1
...         if fallos > 50:
...             print('Se perdio la conexion con la camara')
...             break
...         continue
...     fallos = 0
... 
...     # Haar Cascade trabaja en escala de grises
...     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
... 
...     # Busca la wincha: devuelve una lista de rectangulos (x, y, ancho, alto)
...     toy = WinchaClassif.detectMultiScale(gray,
...                                          scaleFactor=scaleFactor,
...                                          minNeighbors=minNeighbors,
...                                          minSize=minSize)
... 
...     # Dibuja el rectangulo verde y la etiqueta sobre cada deteccion
...     for (x, y, w, h) in toy:
...         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
...         cv2.putText(frame, 'Wincha', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
... 
...     # Muestra la imagen en pantalla
...     cv2.imshow('frame', frame)
... 
...     # Sale con la tecla ESC
...     if cv2.waitKey(1) == 27:
...         break
... 
... # Libera la camara y cierra las ventanas
... cap.release()
