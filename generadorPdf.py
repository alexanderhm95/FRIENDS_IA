from reportlab.pdfgen import canvas
from colorama import Style, init, Fore
import os
def generar_pdf(nombre, texto):
    c = canvas.Canvas(os.getcwd() +"\ArchivosPDF\\"+ nombre+".pdf")
    c.drawString(100,100,texto)
    c.showPage()
    c.save()
    print(Fore.YELLOW+"=============================")
    print(Fore.BLUE+"Archivo generado con exito")
    print(Fore.YELLOW+"=============================")