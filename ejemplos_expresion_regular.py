#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

cadena1 = 'casa'
cadena2 = 'casa'
cadena3 = 'pasa'

if re.match(cadena1, cadena2):
    print('cadena1 y cadena2 son iguales')
else:
    print('cadena1 y cadena2 no son iguales')

if re.match(cadena1, cadena3):
    print('cadena1 y cadena3 son iguales')
else:
    print('cadena1 y cadena3 no son iguales')


# COMODINES    ==> EJEMPLO 1

if re.match('.asa', cadena1) and re.match('.asa', cadena3):
    print('cadena1 y cadena3 terminan en .asa')
else:
    print('cadena1 y cadena3 no terminan en .asa')


# Carácter Especial    ==> EJEMPLO 2

extension1 = '.jpg'
if re.match('.\jpg', extension1):
    print('El archivo es una imagen')

# Alternativas ==> EJEMPLO 3

extensiones = ['jpg', 'png', 'gif', 'mp3', 'doc']

for tipoarchivo in extensiones:
    if re.match('jpg|png|gif|bmp', tipoarchivo):
        print('La extension ', tipoarchivo, 'se corresponde con una imagen')
    else:
        print('La extension ', tipoarchivo, 'no se corresponde con una imagen')

# Grupos Aislados  ==> EJEMPLO 4

palabras = ['careta', 'carpeta', 'colita', 'cateta', 'cocreta', 'caleta', 'caseta']
for termino in palabras:
    if re.match('ca(..|...)ta', termino):
        print(termino)  # careta , carpeta, cateta, caleta, caseta
maspalabras = ['masa', 'mata', 'mar', 'mana','cama', 'marea']
for termino in maspalabras:
    if re.match('ma(s|m|n)a', termino):
        print(termino)  # masa, mana

# Rangos  ==> EJEMPLO 5

codigos = ['se1', 'se9', 'ma2', 'se:','se.', 'se2', 'hu2', 'se3', 'sea', 'sec']

for elemento in codigos:
    if re.match('se[0-5]', elemento):  # el tercer carácter puede ser un nº de 0 a 5
        print(elemento)

for elemento in codigos:
    if re.match('se[0-5a-z]', elemento):  # nº de 0 a 5 y letra de a a z
        print(elemento)

for elemento in codigos:
    if re.match('se[.:]', elemento):  # el tercer carácter puede ser . ó :
        print( elemento)

for elemento in codigos:
    if re.match('se[^0-2]', elemento):  # debe comenzar por nº de 0 a 2
        print(elemento)

# Caracteres predefinidos  ==> EJEMPLO 6

for elemento in codigos:
    if re.match('se\d', elemento):  # el tercer carácter debe ser un número
        print( elemento)

# Caracteres que permiten repeticiones  ==> EJEMPLO 7

codigos = ['aaa111', 'aab11', 'aaa1111', 'aaz1', 'aaa']

for elemento in codigos:
    if re.match('aa[a-z]1{2,}', elemento):
        print(elemento)  # aaa111 , aab11, aaa1111

for elemento in codigos:
    if re.match('a+1+', elemento):
        print(elemento)  # aaa111 , aaa1111

# Coincidencias al comienzo y al final   ==> EJEMPLO 8

lista_url = ['http://www.aaa.es','ftp://www.aaa.es', 'http://www.bbb.es']

for elemento in lista_url:
    if re.match('^ftp://', elemento):
        print(elemento)  # ftp://www.aaa.es

# El objeto mo y el método group()   ==> EJEMPLO 9

mo = re.match('ftp://.+\com', 'ftp://ovh.com')
print(mo.group())  # ftp://ovh.com

    # Con los paréntesis acotamos los grupos:

mo = re.match('ftp://(.+)\com', 'ftp://ovh.com')
print(mo.group(0))  # ftp://ovh.com
print(mo.group(1))  # ovh.
print(mo.groups())  # ('ovh.',).


# La función search()    ==> EJEMPLO 10

palabras = ['paniaguado', 'agüita', 'aguador', 'paraguas', 'agua']

for elemento in palabras:
    if re.search('agua', elemento):
        print( elemento)  # muestra: paniaguado, aguador , paraguas, agua

