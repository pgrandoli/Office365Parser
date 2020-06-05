#!/usr/bin/python3

# Importar librerias
import json
import urllib.request


# Descargar JSON desde Microsoft
with urllib.request.urlopen("https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7") as url:
    data = json.loads(url.read().decode())


# Se define lista
url = []


# Se filtra JSON y solo queda valor de URLs
for item in data:
    url.append(item.get("urls"))


# Se convierte la lista a string
url_flattened = str(url)

# Se remueven caracteres, se termina de filrar
url_newline = url_flattened.replace(', ' , '\n')
url_newline = url_newline.replace('[', '')
url_newline = url_newline.replace(']', '')
url_newline = url_newline.replace("'", '')


# Se imprime URLs en archivo de texto
print("[block]\n" + url_newline + "\n[allow]\n", file = open("Exclusiones.txt", "w"))
