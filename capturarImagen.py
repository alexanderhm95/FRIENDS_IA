import cv2
import os
from colorama import Style, init, Fore
init()
def capturar():
    llave = True
    ruta=""
    while(llave):
        cap = cv2.VideoCapture(0)
        flag = cap.isOpened()
        index = 1
        ruta=""
        print(Fore.YELLOW+"Presione 's' para guardar\n"+Fore.RED+"Presione 'q' para salir\n")
        while(flag):
            ret, frame = cap.read()
            cv2.imshow("Capturar texto",frame)
            k = cv2.waitKey(1) 
            if k == ord('s'): #Presione la tecla s para ingresar a la siguiente operación de guardado de imágenes
                cv2.imwrite(os.getcwd() +"\imagenes\\"+ str(index) + ".jpg", frame)
                ruta=os.getcwd() +"\imagenes\\"+ str(index) + ".jpg"
                print(Fore.GREEN+"save" + str(index) + ".jpg guardado con exito!")
                print("--------------------------------------------")
                index += 1
                llave=False
                cap.release()
                cv2.destroyAllWindows()

                rs=ruta.replace('\\\\', '/')

                imagen=cv2.imread(rs,1)
                cv2.imshow('Captura',imagen)
                cv2.waitKey(0)
                break
            elif k == ord('c'): #Presione la tecla c para capturar nuevamente    
                llave=True
            elif k == ord('q'): #Presione la tecla q, el programa sale
                llave=False
                break
        cap.release()
        cv2.destroyAllWindows()
    return ruta
