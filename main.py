#!/usr/bin/python3
from colorama import Style, init, Fore

from tkinter import *
from tkinter import filedialog
import capturarImagen
import scanner
import detectorTexto
import textoVoz
import generadorPdf
import traductor

init()
#Funcion de control para el menu de opciones 
def pedirNumeroEntero(): 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(Fore.YELLOW+'Introduce un numero entero: '))
            correcto=True
        except ValueError:
            print(Fore.RED+'Error, introduce un numero entero')
     
    return num

salir = False
opcion = 0
 
while not salir:
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")
    print( Style.RESET_ALL + Fore.GREEN + "########             LECTURA ORC            #####")
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")
    print (Fore.WHITE+"1. Cargar imagen")
    print (Fore.WHITE+"2. Capturar imagen")
    print (Fore.WHITE+"3. Salir")
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")
    opcion = pedirNumeroEntero()
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")

#La opcion 1 permite cargar una imagen desde una ruta espesifica
    if opcion == 1:
        #cargar imagen
        root = Tk()
        root.archivo = filedialog.askopenfilename(title="Abrir")
        root.withdraw()
        
        #escanear imagen
        textScan=scanner.escanear(root.archivo)

        #deteccion de idioma
        detectorTexto.language_detection_example(textScan)
        
        #opciones de salida
        salir2 = False
        opcion2 = 0
        while not salir2:
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            print( Style.RESET_ALL + Fore.GREEN + "########          Opciones de Salida        #####")
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            print (Fore.WHITE+"1. Traducir")
            print (Fore.WHITE+"2. Voz")
            print (Fore.WHITE+"3. Pdf")
            print (Fore.WHITE+"4. Salir")
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            opcion2 = pedirNumeroEntero()
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            if opcion2 == 1:
                print("Escriba el tipo de idioma a traducir\nEjemplo para el ingles escriba: en ")
                print("Revise la documentacion para revisar los idiomas disponibles")
                print("'en', 'es', 'fr', 'it', 'de', 'ja', 'ko', 'pt'\n, 'ru', 'zh-Hans', 'zh-Hant', 'yue', 'wyw', 'yue'\n, 'zh-CHS', 'zh-CHT' ")
                text_out=input(Fore.YELLOW+'Introduce el idioma: ')
                traductor.traducir(textScan,'es',text_out)
            elif opcion2 == 2:
                #Escuchar Voz
                textoVoz.texto_avoz(textScan)

            elif opcion2 == 3:
                #Generación de PDF
                nombreArchivo=input(Fore.YELLOW+'Introduce el nombre del archivo: ')
                generadorPdf.generar_pdf(nombreArchivo,textScan)
            elif opcion2 == 4:
                salir2 = True
            else:
                print ("Introduce un numero entre 1 y 4")
                print( Style.RESET_ALL + Fore.GREEN + "#################################################")
#La opcion 2 permite capturar una imagen desde la camara
    elif opcion == 2:
        #Abrir y capturar imagen con camara 
        texto=capturarImagen.capturar()
        
        #Escaner de contenido
        textScan=scanner.escanear(texto)

        #deteccion de idioma
        detectorTexto.language_detection_example(textScan)
        
        #opciones de salida
        salir2 = False
        opcion2 = 0
        while not salir2:
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            print( Style.RESET_ALL + Fore.GREEN + "########          Opciones de Salida        #####")
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            print (Fore.WHITE+"1. Traducir")
            print (Fore.WHITE+"2. Voz")
            print (Fore.WHITE+"3. Pdf")
            print (Fore.WHITE+"4. Salir")
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            opcion2 = pedirNumeroEntero()
            print( Style.RESET_ALL + Fore.GREEN + "#################################################")
            if opcion2 == 1:
                print("Escriba el tipo de idioma a traducir\nEjemplo para el ingles escriba: en ")
                print("Revise la documentacion para revisar los idiomas disponibles")
                print("'en', 'es', 'fr', 'it', 'de', 'ja', 'ko', 'pt'\n, 'ru', 'zh-Hans', 'zh-Hant', 'yue', 'wyw', 'yue'\n, 'zh-CHS', 'zh-CHT' ")
                text_out=input(Fore.YELLOW+'Introduce el idioma: ')
                traductor.traducir(textScan,'es',text_out)

            elif opcion2 == 2:
                #Escuchar Voz
                textoVoz.texto_avoz(textScan)

            elif opcion2 == 3:
                #Generación de PDF
                nombreArchivo=input(Fore.YELLOW+'Introduce el nombre del archivo: ')
                generadorPdf.generar_pdf(nombreArchivo,textScan)
            elif opcion2 == 4:
                salir2 = True
            else:
                print ("Introduce un numero entre 1 y 4")

    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

print( Style.RESET_ALL + Fore.GREEN + "#################################################")
print( Style.RESET_ALL + Fore.GREEN + "########         FIN LECTURA ORC            #####")
print( Style.RESET_ALL + Fore.GREEN + "#################################################")