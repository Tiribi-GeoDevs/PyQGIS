"""
Corrección y actualización topológica
Desarrollado por: JDGG - ADCHP
Agradecimientos: KCS - HGA
Fecha: 7/2/22
"""

## Capa a corregir (realizar en temporal antes de ejecutar en terreno)
terreno = iface.activeLayer() ##capa a corregir

clone_layer = processing.run("native:saveselectedfeatures", {'INPUT': terreno, 'OUTPUT': 'memory:'})

## Parámetros herramienta "Ajustar geometrias a capa"
params_ajust = {
    'BEHAVIOR': 0,
    'INPUT': clone_layer['OUTPUT'],
    'REFERENCE_LAYER': clone_layer['OUTPUT'],
    'TOLERANCE': 0.2, ## Modificar según criterio
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
}

## Herramienta "Ajustar geometrias a capa"
capa_2 = processing.run("native:snapgeometries", params_ajust)

## Salida
capa_2 = capa_2['OUTPUT']

## Parámetros herramienta "Corrregir geometrias"
params_fix = {
    'INPUT': capa_2,
    'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
}

## Herramienta "Corrregir geometrias"
capa_3 = processing.run("native:fixgeometries", params_fix)

## Salida
capa_3 = capa_3['OUTPUT']

## QgsProject.instance().addMapLayer(capa_3)

## Extraer objetos de capa corregida enlistados
capa_3_obs = list(capa_3.getFeatures())

## Abrir edición de capa a corregir
terreno.startEditing()

## Loop de actualización de geometría
for a in capa_3_obs:
    correc_t_id = a.attributes()[0]
    correc_geo = a.geometry()
    poli_t = list(terreno.getFeatures(f"t_id = {correc_t_id}"))[0]
    fid_t = poli_t.id()
    terreno.changeGeometry(fid_t, correc_geo)
    terreno.commitChanges(stopEditing = False)

## Detener edición
terreno.rollBack()

## Fin de código

#terreno = iface.activeLayer()
#layer.selectAll()
#clone_layer = processing.run("native:saveselectedfeatures", {'INPUT': layer, 'OUTPUT': 'memory:'})['OUTPUT']
#layer.removeSelection()
#QgsProject.instance().addMapLayer(clone_layer)