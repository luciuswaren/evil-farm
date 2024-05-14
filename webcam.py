import cv2
import urllib.request
import numpy as np
import time

# URL de la cámara web
url = "URL_DE_LA_CAMARA" # Código qr con acceso a la oficina de Administrador de sistema

# Función para capturar la imagen desde la URL
def capturar_imagen(url):
    # Intenta abrir la URL y leer la imagen
    try:
        img_resp = urllib.request.urlopen(url)
        img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        img = cv2.imdecode(img_np, -1)
        return img
    except Exception as e:
        print("Error al capturar la imagen:", e)
        return None

# Función para imprimir una animación simple
def imprimir_animacion(frames, velocidad=0.1):
    for frame in frames:
        print(frame, end='\r')
        time.sleep(velocidad)

# Bucle principal para capturar imágenes continuamente
while True:
    # Capturar imagen desde la URL
    imagen = capturar_imagen(url)
    
    # Mostrar una animación de "hackeo"
    imprimir_animacion(["HACKING...", "ACCEDIENDO A LA CÁMARA...", "OBTENIENDO IMAGEN..."])
    
    # Mostrar la imagen si se pudo capturar
    if imagen is not None:
        cv2.imshow("Cámara Hackeada", imagen)
    else:
        print("Error: No se pudo obtener la imagen de la cámara.")
    
    # Esperar 1 segundo y salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()
