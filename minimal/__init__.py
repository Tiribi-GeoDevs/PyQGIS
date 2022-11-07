#-----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

# Plugin minimal by Victor Olaya
# Crear carpeta en el perfil de QGIS en plugins (init.py - metadata.txt)
# C:\Users\jorge\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\minimal
# Plantilla de: https://github.com/wonder-sk/qgis-minimal-plugin
 
# librerias
from PyQt5.QtWidgets import *
from qgis.gui import QgsProjectionSelectionDialog

# Función para definir sistema de coordenadas
def setProjectCrs():
	dialog = QgsProjectionSelectionDialog()
	if dialog.exec_():
		crs = dialog.crs()
		QgsProject.instance().setCrs(crs)

# función para llamar el método del plugin
def classFactory(iface):
    return ProjectCrsPlugin(iface)

# Método del plugin:
class ProjectCrsPlugin:
	def __init__(self, iface):
		self.iface = iface
		iface.newProjectCreated.connect(setProjectCrs)
	
	def initGui(self):
		pass
	
	def unload(self):
		self.iface.newProjectCreated.disconnect(setProjectCrs)

# Fin codigo