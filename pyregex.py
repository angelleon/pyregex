#!/bin/env python3
# -*- coding: utf8 -*-
import re
import sys
import os.path

"""
El siguiente programa usa los metodos de la clase re de la libreria estandar
de python 3 para evaluar expresiones regulares en cadenas y, opcionalmente,
archivos de texto
"""

"""
pyregex.py

Copyright 2017 Angel Leon <luianglenlop@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""


def evaluar(regex, texto_entrada, flags=None):  # 'core' del programa
	try:  # Se lanza una excepcion cuando se pasa una regex incorrecta a re.compile
		motor = re.compile(regex)
	except Exception:
		print("Regex incorrecta")
		return None
	resultado = []
	for linea in texto_entrada:
		if flags is not None and flags:
			coincidencias = motor.findall(linea, re.IGNORECASE)
		else:
			coincidencias = motor.findall(linea)
		resultado.append(coincidencias)
	if len(resultado) == 0:
		return None
	texto_salida = ""
	cont = 0
	for i in resultado:
		if len(i) != 0:
			texto_salida += texto_entrada[cont] + '\n'
		cont += 1
	return texto_salida


def main(argv):  # definicion de la funcion principal, preparar parametros para pasar a 'evaluar'
	if len(argv) == 1:
		return None
	elif len(argv) < 3:  # minimo 2 parametros, el primero es la llamada a este script
		print("Sintaxis: pyregex REGEX -m (STRIG1 [STRING2] ... [STRINGN]| -f ARCHIVO1 [ARCHIVO2] ... [ARCHIVON])")
		return None
	regex = argv[1]  # obtener regex
	argv = argv[2:]  # obtener los demas parametros
	# print(regex)
	# print(argv)
	cont = 0
	flags = None
	mensaje = ''
	texto_entrada = []
	for i in argv:
		# print(i)
		if i == "-f" and cont != len(argv) - 1:
			if i == "-f":
				continue  # no evalua el modificador
			if os.path.isfile(i):  # comprueba existencia del archivo
				with open(i, "r") as f:
					i = f.read()  # obtener texto_entrada
					i = i.splitlines()  # dividir texto_entrada
			else:
				mensaje += i + ' no se encontro en el sistema de archivos\n'
		if i == "-m":
			flags = True  # Ignorar capitalizacion
		texto_entrada.append(i)
	resultado = evaluar(regex, texto_entrada, flags)  # Llamada a 'evaluar'
	print(resultado)

if __name__ == '__main__':
	# print(sys.argv)
	# print(len(sys.argv))
	main(sys.argv)
