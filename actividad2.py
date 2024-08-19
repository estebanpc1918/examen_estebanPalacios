from PIL import Image
import os

ruta_ft = '/home/usuario/Desktop/examen_19_08/img/cara.jpeg'
foto = Image.open(ruta_ft)
foto.show()

foto_copy = foto.copy()

nombre_ft = 'cara_copia.jpg'

ruta_copia = os.path.join(os.getcwd(), nombre_ft)
foto_copy.save(ruta_copia)
print('la copia de la foto se guardo')