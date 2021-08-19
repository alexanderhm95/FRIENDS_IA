import os, requests, time 
from xml.etree import ElementTree
import uuid, json

#Credenciales para el traductor
subscription_key = "b1b5a26542ea49bcb31c976abbbcdcc3"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "southcentralus"

def traducir(texto,idioma_in,idioma_out):
    # Crear una instancia de la clase Translator
    path = '/translate'
    constructed_url = endpoint + path
    #Parámetros de traducción
    params = {
        'api-version': '3.0',
        'from': idioma_in,
        'to': [idioma_out]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text':texto
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = json.loads(request.text)
    textoTraducido=response[0]['translations'][0]['text']
    print(textoTraducido)
