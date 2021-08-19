from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
from colorama import Style, init, Fore
import os
from PIL import Image
import sys
import time

# <Credenciales>
subscription_key = "b7b8812cfb7841028d7a012a71a9539a"
endpoint = "https://friendsiaorc.cognitiveservices.azure.com/"

# Autenticacion

try:
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    print("Acceso correcto")		
except Exception as err:
    print("Problema de autenticacion. {}".format(err))


def escanear(ruta):
    textoEscaneado=""
    images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
    print("===== Leyendo archivo local...")
    # Obteniendo el path de la imagen
    read_image_path = os.path.join (images_folder, ruta)
    # Abriendo la imagen
    read_image = open(read_image_path, "rb")
    # llamando a la API 
    read_response = computervision_client.read_in_stream(read_image, raw=True)
    # Get the operation location (URL with ID as last appendage)
    read_operation_location = read_response.headers["Operation-Location"]
    # Take the ID off and use to get results
    operation_id = read_operation_location.split("/")[-1]
    # Call the "GET" API and wait for the retrieval of the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower () not in ['notstarted', 'running']:
            break
        print ('Waiting for result...')
        time.sleep(10)

    # Print results, line by line
    if read_result.status == OperationStatusCodes.succeeded:

        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                textoEscaneado = textoEscaneado + line.text + "\n"
                print(line.text)
                #print(line.bounding_box)
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")
    print( Style.RESET_ALL + Fore.GREEN + "########         Archivo Leido              #####")
    print( Style.RESET_ALL + Fore.GREEN + "#################################################")
    return textoEscaneado
    