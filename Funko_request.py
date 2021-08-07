from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
from openpyxl import *

pag_url = "https://www.funkopopstore.com.ar/productos/?orderby=stock_quantity_desc"  # url de la pagina
pag_url2 = "https://www.funkopopstore.com.ar/productos/page/2/?orderby=stock_quantity_desc"

print(pag_url2.replace("2", "3"))

uClient = uReq(pag_url)  # abro la pagina con ureq

pag_soup = soup(uClient.read(), "html.parser")  # cargo la pagina bs
uClient.close()  # cierro ureq

# creo archivo para guardar datos
wb = Workbook()
nombre_archivo = "./prueba.xlsx"
wb.save(nombre_archivo)
wb = load_workbook(nombre_archivo)
sheet = wb.active

sheet["A4"] = 56
sheet["A2"] = 56
b = 1
linea = "A"
print(linea)
# abrirlo y crearlo


dias_anteriores = 3
containers = pag_soup.findAll("figure", {"class", "woocom-project"})
datos = {}
for contain in containers:
    nombre = contain.figcaption.h4.a.text
    precio = contain.figcaption.span.text
    sheet[linea + str(b)] = nombre
    #sheet [linea_precio] = precio
    datos[nombre] = precio
    b += 1
wb.save(nombre_archivo)
# Buscar un producto

