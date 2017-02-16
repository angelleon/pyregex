#!/bin/env python3
# -*- coding: utf8 -*-
import sys
from pyregex import evaluar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QCheckBox,
							QDesktopWidget, QLineEdit, QMessageBox,
							QHBoxLayout, QVBoxLayout, QWidget, QPlainTextEdit, QMenuBar)
"""
El siguiente programa usa el framework Qt5 para construir la interfaz grafica de usuario (frontend)
para el la función 'evaluar' del modulo pyregex (tambien escrito por mi)
"""

"""
qpyregex.py

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


class Gui(QWidget):
	def __init__(self):  # Constructor de clase para la interfaz grafica
		super().__init__()
		caja_v = QVBoxLayout()
		caja_regex = QHBoxLayout()
		menu_bar = QMenuBar()
		menu_bar.addAction("About", self.about)
		self.txt_regex = QLineEdit()
		self.txt_a_tratar = QPlainTextEdit()
		self.txt_coincidencias = QPlainTextEdit()
		btn_probar = QPushButton("Probar")
		caja_regex.addWidget(QLabel("Expresión:"))
		caja_regex.addWidget(self.txt_regex)
		caja_regex.addWidget(btn_probar)
		self.chk_case = QCheckBox("Mayúsculas")
		caja_opciones = QHBoxLayout()
		caja_opciones.addWidget(QLabel("Texto a tratar:"))
		caja_opciones.addStretch(1)
		caja_opciones.addWidget(self.chk_case)
		caja_v.setMenuBar(menu_bar)
		caja_v.addLayout(caja_regex)
		caja_v.addLayout(caja_opciones)
		caja_v.addWidget(self.txt_a_tratar)
		caja_v.addWidget(QLabel("Coincidencias:"))
		caja_v.addWidget(self.txt_coincidencias)
		btn_probar.pressed.connect(self.evaluar)
		self.txt_regex.pyqtConfigure(clearButtonEnabled=True)
		self.txt_regex.pyqtConfigure(placeholderText="Inserte su regex")
		self.txt_regex.textEdited.connect(self.reset)
		self.txt_a_tratar.pyqtConfigure(placeholderText="Insete su texto a tratar")
		self.txt_coincidencias.setReadOnly(True)
		self.setLayout(caja_v)
		self.setWindowTitle("Evaluador de RegEx")
		self.setWindowIcon(QIcon("zorro.png"))
		self.resize(400, 350)
		self.centrar()
		self.show()

	def evaluar(self):
		self.txt_coincidencias.pyqtConfigure(plainText='')
		regex = self.txt_regex.text()  # Obtener expresion regular
		texto_entrada = self.txt_a_tratar.toPlainText()  # Obtener del campo de texto
		texto_entrada = texto_entrada.splitlines()
		if regex == "":  # Validar si regex es cadena nula
			return None
		if self.chk_case.checkState():
			texto_salida = evaluar(regex, texto_entrada, True)
		else:
			texto_salida = evaluar(regex, texto_entrada, None)
		if texto_salida is not None:
			self.txt_coincidencias.pyqtConfigure(plainText=texto_salida)  # Mostrar en el campo de texto los resultados
		else:
			self.txt_regex.setStyleSheet("background-color: red; color: white")

	def centrar(self):  # Centrar la ventana respecto al escritorio
		fg = self.frameGeometry()
		fg.moveCenter(QDesktopWidget().availableGeometry().center())
		self.move(fg.topLeft())

	def reset(self):  # Regresar a colores por defecto campo de regex cuando se ha corregido regex erronea
		self.txt_regex.setStyleSheet("")

	def about(self):  # Credito al programador (yo) y al diseñador del icono de la aplicacion
		info = "<b>Evaluador de RegEx</b><br>Copyright \u00a9 2017 Ángel León López</br><br>Este programa es software " \
		       "libre licenciado bajo la GNU GPL3</br><br>Fox icon designed by <a " \
		       "href=http://www.flaticon.com/authors/freepik>Freepik from Flaticon</a></br>"
		mensaje = QMessageBox()
		mensaje.setWindowTitle("Acerca de...")
		mensaje.setText(info)
		mensaje.setIconPixmap(QPixmap("panda.png"))
		mensaje.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Gui()
	sys.exit(app.exec_())
