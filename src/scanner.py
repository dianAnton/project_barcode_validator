# Etapa 0.1 del programa de escaneo en tiempo real

# El programa abrira la camara en tiempo real y buscara codigos comprobando si coinciden con las reglas o no

import cv2
from pyzbar.pyzbar import decode

# Importamos del modulo de la base de datos la funcion get_product_rule
from database import get_product_rule

def main():

    # Creamos el objeto que permite captura el video. Objeto VideoCapture
    # El index 0 toma la camara por defecto
    cap = cv2.VideoCapture(0)

    # Informacion de debuggeo
    print("[INFO] Iniciando sistema de validacion de codigos...")
    print("[INFO] Presiona 'q' en el teclado para salir.")

    # Manejo de errores. Caso donde comprobamos que la camara no se pudo abrir
    if not cap.isOpened():
        print("La camara no se pudo abrir")
        exit()
    
    # Mientras la camara este abierta exitosamente
    while cap.isOpened():

        # Captura frame a frame. ret es el valor de retorno. 
            # ret sera TRUE si todos los frames son leidos correctamente.  
        ret, frame = cap.read()

        if not ret:
            print("[ERROR] No se pudo acceder a la camara correctamente")
            break

        # Decodificar el codigo de barras en el frame actual
        decoded_objects = decode(frame)

        # Recorrer cada codigo encontrado
        for obj in decoded_objects:

            # Convertimos obj.data en un string manejable por python, decodificandolo utilizando UTF-8    
            ean_data = obj.data.decode('utf-8')

            # Obtenemos las coordenadas exactas. Luego OpenCV sabra donde dibujar en pantalla
            point = obj.rect

            # Consultamos regla en la base de datos
                # RECUERDA QUE LA BASE DE DATOS ES UNA PRUEBA. 
            rule = get_product_rule(ean_data)

            # Comprobamos y avisamos mediante output visual, si la regla fue exitosamente encontrada o no.
            if rule:
                text = f"OK: {rule['sku']}"

                # Color verde
                color = (0, 255, 0)
                
            else:
                text = f"DESCONOCIDO: {ean_data}"

                # Color rojo
                color = (0, 0, 255) 

            # Dibujar rectángulo y texto sobre el frame de video
            cv2.rectangle(frame, (point.left, point.top), (point.left + point.width, point.top + point.height), color, 3)
            cv2.putText(frame, text, (point.left, point.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Mostrar la ventana con la interfaz de video de OpenCV
        cv2.imshow("Validador de codigos - TEST", frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


        

