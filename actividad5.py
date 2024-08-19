from PIL import Image
import os , sys


ruta_foto = input('ingrese la ruta de la foto: ')
foto= Image.open(ruta_foto)

ruta_marca = input('ingrese la ruta de la marca de agua: ')
foto_marc = Image.open(ruta_marca)

margen = 50

print('Seleccione donde quiere que vaya la marca de agua')
print('Escriba 1, 2, 3, 4')
print('\t1_arriba a la izquierda')
print('\t2_arriba a la derecha')
print('\t3_abajo a la izquierda')
print('\t4_abajo a la derecha')
ubicacion = input()

if ubicacion not in ['1', '2', '3', '4']:
    sys.exit('Error: Usted debía ingresar 1, 2, 3, 4')
else:
    image_new = foto.copy()

    
    if foto_marc.mode != 'RGBA':
        foto_marc = foto_marc.convert('RGBA')

    alpha_mask = foto_marc.split()[3]

    if ubicacion == '1':
        image_new.paste(foto_marc, (margen, margen), mask=alpha_mask)
    elif ubicacion == '2':
        pos_x = foto.width - foto_marc.width - margen
        image_new.paste(foto_marc, (pos_x, margen), mask=alpha_mask)
    elif ubicacion == '3':
        pos_y = foto.height - foto_marc.height - margen
        image_new.paste(foto_marc, (margen, pos_y), mask=alpha_mask)
    else:
        pos_x = foto.width - foto_marc.width - margen
        pos_y = foto.height - foto_marc.height - margen
        image_new.paste(foto_marc, (pos_x, pos_y), mask=alpha_mask)

    ruta_salida = 'foto_marcadaaa.jpeg'
    image_new.save(ruta_salida)
    print(f'La imagen con marca de agua ha sido guardada como {ruta_salida}')
    image_new.show()
