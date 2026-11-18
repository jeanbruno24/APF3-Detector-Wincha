# Captura de imagenes NEGATIVAS (fondos SIN la wincha: pared, mesa, manos, otros objetos)
# Tecla 's' = guardar imagen | ESC = salir
import cv2
import imutils
import os

Datos = "n"              # carpeta de negativas
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture("http://10.113.163.222:4747/video")
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

x1, y1 = 350, 60
x2, y2 = 740, 450

count = len([f for f in os.listdir(Datos) if f.endswith('.jpg')])
fallos = 0

while True:
    ret, frame = cap.read()
    if not ret:
        fallos += 1
        if fallos > 50:
            print('Se perdio la conexion con la camara')
            break
        continue
    fallos = 0

    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.putText(frame, 'Negativas: {}'.format(count), (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=38)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), objeto)
        print('Imagen guardada: ' + Datos + '/objeto_{}.jpg'.format(count))
        count += 1
    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()
