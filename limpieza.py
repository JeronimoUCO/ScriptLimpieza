#Se importan las librerias necesarias para manipular los datos
import pandas as pd

#Si el archivo está en la misma carpeta que el Script es el nombre del archivo, de lo contrario es la ruta de este
nombre_archivo= input("Escriba el nombre del archivo (con extension) en el que están almacenados los datos que va a limpiar: ")
ruta_archivo=f"Archivo/{nombre_archivo}"

tabla=pd.read_csv(ruta_archivo,sep="\t",header=0,encoding="UTF-8")

#Se eliminan las columnas en las que todos los datos sean nulos
tabla = tabla.dropna(axis=1,how="all")

#Se eliminan las filas en las que todos los datos sean nulos
tabla = tabla.dropna(axis=0,how="all")

#En las celdas en las que hayan datos faltantes,se reemplazan por 0
tabla=tabla.fillna(0)

#Se sobreescribe el archivo ingresado
tabla.to_csv("Archivo/paciente.tsv", sep="\t",index=False,encoding="UTF-8")