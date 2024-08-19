from PIL import Image
import os

ruta_ft = '/home/usuario/Desktop/examen_19_08/img/cara.jpeg'
foto = Image.open(ruta_ft)
foto.show()

#nobre
nom_ft = os.path.basename(ruta_ft)
print(f'nombre {nom_ft}')
#extencion
print(f'extencion {foto.format}')
#resolucion
whidth, height = foto.size
print(f'resolucion {whidth}x{height}')
#cantidaad de pixeles
cant_pixel = whidth*height
print(F'cantidad de pixeles {cant_pixel}')
#ruta
print(f'ruta {foto.filename}')
