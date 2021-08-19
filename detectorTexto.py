from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import credenciales

#Autenticacion de la API de azure
client = credenciales.authenticate_client()
def language_detection_example(text):
    try:
        documents = [text]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Idioma detectado: ", response.primary_language.name)		
    except Exception as err:
        print("Error al detectar idioma. {}".format(err))