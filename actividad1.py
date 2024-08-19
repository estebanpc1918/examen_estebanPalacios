from PIL import Image
import os

ruta_foto = input('ingrese la ruta de la foto: ')
foto = Image.open(ruta_foto)
foto.show()

#nobre
nom_ft = os.path.basename(ruta_foto)
print(f'nombre: {nom_ft}')
#extencion
print(f'extencion: {foto.format}')
#resolucion
whidth, height = foto.size
print(f'resolucion: {whidth}x{height}')
#cantidaad de pixeles
cant_pixel = whidth*height
print(F'cantidad de pixeles: {cant_pixel}')
#ruta
print(f'ruta {foto.filename}')