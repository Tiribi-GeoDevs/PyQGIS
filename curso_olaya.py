# Llamar capa a partir de ruta (path)
layer_1 = QgsVectorLayer('C:/Users/jorge/Downloads/curso-qgis-python-master/datos/ne_110m_admin_0_countries.shp', 
'capa')

# Crear variable con la capa activa del proyecto QGIS
layer = iface.activeLayer()

# Obtener iterador de los registros de la capa en una lista
features = list(layer.getFeatures())

# Imprimir el valor del primer registro de la columna "wikipedia"
print(features[0]["wikipedia"])

fieldpob = [f["POP_EST"] for f in features]
suma = sum(fieldpob)
print(suma)

fieldpob_eu = [f["POP_EST"] for f in features if f["CONTINENT"] == "Europe"]
fieldpob_eu = [f["POP_EST"] for f in layer.getFeatures('"CONTINENT" = \'Europe\'')]
suma_ue = sum(fieldpob_eu)
print(suma_ue)

layer_2 = QgsVectorLayer("Point?crs=EPGS:4326", "capa_2", "memory")
field = QgsField("id", QVariant.String)
layer_2.dataProvider().addAttributes([field])
layer_2.addAttribute(field)
layer_2.updateFields()
layer_2.fields().toList()

feature = QgsFeature()
feature.setFields(layer_2.fields())
feature.setAttributes(["1"])
feature.setAttribute(0, "2")
feature.setAttribute("id", "3")

pt = QgsPointXY(1, 1)
geom = QgsGeometry.fromPointXY(pt)
geom.asWkt()
feature.setGeometry(geom)
layer_2.dataProvider().addFeatures([feature])

import random

def createLayer(n):
    layer = QgsVectorLayer("Point?crs=EPSG:4326", "capa", "memory")
    field = QgsField("id", QVariant.Int)
    layer.dataProvider().addAttributes([field])
    layer.updateFields()
    features = []
    for i in range(n):
        feature = QgsFeature()
        feature.setFields(layer.fields())
        x = random.uniform(-180, 180)
        y = random.uniform(-90, 90)
        pt = QgsPointXY(x, y)
        geom = QgsGeometry.fromPointXY(pt)
        feature.setGeometry(geom)
        feature.setAttribute(0, i)
        features.append(feature)
    layer.dataProvider().addFeatures(features)
    return layer

randomLayer = createLayer(50)
print(len(list(randomLayer.getFeatures())))
QgsProject.instance().addMapLayer(randomLayer)