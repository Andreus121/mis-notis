#mi primer intento para extraer contenido de una pagina
import requests
from bs4 import BeautifulSoup

def extraer_datos_producto(url):
    #----VARIABLES INICIALES----
    #esta configuración es para simular ser un usuario en un navegador
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    #ingresa a la url con la configuracion asignada antes en headers
    respuesta = requests.get(url, headers=headers)
    #la estructura html de la pagina
    html = respuesta.text

    #----COMPROBAR CONEXION A LA PAGINA----
    #comprobar conexion con la pagina
    if  respuesta.status_code != 200:
        print(f"Error al ingresar a la pagina, código: {respuesta.status_code}")
        return None #corta la función

    #----EXTRACCIÓN NOMBRE----
    sopa = BeautifulSoup(html, 'html.parser') #html desordenado
    producto_nombre = sopa.find('h1', class_='ui-pdp-title') #da true si encuentra algo
    if producto_nombre:
        producto_nombre = producto_nombre.get_text() #limpia el codigo html del texto deseado
    else:
        producto_nombre = "Producto no encontrado"

    #----EXTRACCIÓN PRECIO----
    producto_precio = sopa.find('span',class_='andes-money-amount__fraction')
    if producto_precio:
        #quita los html, el punto del numero y lo pasa a int
        producto_precio = int(producto_precio.get_text().replace(".","")) 
    else:
        producto_precio = 0
    
    return {
        "nombre": producto_nombre,
        "precio": producto_precio
    }


if __name__ == "__main__":
    url_prueba = "https://www.mercadolibre.cl/peluche-tralalero-tralala-ballerina-capuchina-brainot/up/MLCU3243300971#polycard_client=search-nordic&search_layout=grid&position=13&type=product&tracking_id=7c84665c-b4da-43a0-9cf0-28b36ef885e2&wid=MLC2929889998&sid=search"
    datos = extraer_datos_producto(url_prueba)

    if datos:
        print("Datos extraidos correctamente")
        print(f"Nombre: {datos['nombre']}")
        print(f"Precio: {datos['precio']}")
    else:
        print("No se pudieron extraer los datos")


