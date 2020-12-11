"""
En este script se graba un video con la web-cam y se guarda en una carpeta
usando Open CV
"""

import cv2

# Adquirimos la imagen de la web-cam
captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('video_salida.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640, 480))
while(captura.isOpened()):
    ret, img = captura.read()
    if ret == True:
        cv2.imshow('Video', img)
        salida.write(img)
        if cv2.waitKey(1) and 0xFF == ord('s'):
            break

captura.release()
salida.release()
cv2.destroyAllWindows()
