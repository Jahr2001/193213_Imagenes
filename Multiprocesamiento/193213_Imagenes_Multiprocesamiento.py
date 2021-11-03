from imgurpython import ImgurClient
##
from multiprocessing import Pool
##
import os
import urllib.request
import timeit

listaUrls = []  #Lista para guardar las Urls de las imagenes

secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
 
def descarga_url_img(link):
   #print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "D:\\Documentos\\7mo Cuatrimestre\\Programación Concurrente\\Segundo Corte\\193213_Imagenes\\Multiprocesamiento\\Imagenes\\{}.{}"
   
   #Guardar en local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 

def main():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
 
   for imagen in imagenes:
       descarga_url_img(imagen.link)#Descarga las imagenes
       listaUrls.append(imagen.link) #Se agrega la url de cada una de las imagenes en la lista

def multiprocesamiento():
    print('\n Multiprocesamiento')
    pool = Pool(len(listaUrls)) #grupo de procesos que llevarán a cabo las tareas que se le presenten con la clase Pool
    pool.map(descarga_url_img, listaUrls)# map() toma la función que queremos paralelizar y un iterable como los argumentos.

if __name__ == "__main__":
   print(f'Tiempo de descarga Sincrono: {timeit.Timer(main).timeit(number=1)}')
   print(f'Tiempo de descarga Multiprocesamiento: {timeit.Timer(multiprocesamiento).timeit(number=1)}')
   
   #193213 - José Alberto Hernández Ramírez