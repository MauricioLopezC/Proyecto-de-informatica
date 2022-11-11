import os #para manipular archivos y directorios
import datetime #para obtener datos de la fecha
datos_f = str(datetime.datetime.now()).split(".")
datos_f = datos_f[0]

def file_move ():
    carpeta_actual = os.getcwd() + "/"#obener el directio de trabajo actual
    carpeta_historial = carpeta_actual + "historial/"

    for nombre_archivo in os.listdir(carpeta_actual):
        nombre, extension = os.path.splitext(carpeta_actual + nombre_archivo)
        nombre = nombre_archivo.split(".")
        nuevo_nombre = nombre[0] + datos_f + extension
        if extension == ".xlsx":
            os.rename(carpeta_actual + nombre_archivo, carpeta_historial + nuevo_nombre)
