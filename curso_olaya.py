# Llamar capa a partir de ruta (path)
layer_1 = QgsVectorLayer('C:/Users/jorge/Downloads/curso-qgis-python-master/datos/ne_110m_admin_0_countries.shp', 
'capa')

# Crea variable con la capa activa del proyecto QGIS
layer = iface.activeLayer()

# Obtener iterador de los registros de la capa en una lista
features = list(layer.getFeatures())

# Imprimir el valor del primer registro de la columna "wikipedia"
print(features[0]["wikipedia"])

# Crea variable con los datos de todos los registros de la columna "POP_EST" en una lista
fieldpob = [f["POP_EST"] for f in features]

# Crea variable con la suma de todos los registros de "POP_EST", población total.
suma = sum(fieldpob)
print(suma)

# Crea variable con los registros de la columna "POP_EST", filtrados solo para Europa.
fieldpob_eu = [f["POP_EST"] for f in features if f["CONTINENT"] == "Europe"]
fieldpob_eu = [f["POP_EST"] for f in layer.getFeatures('"CONTINENT" = \'Europe\'')]

# Crea variable con la suma de los registros de "POP_EST", población europea.
suma_ue = sum(fieldpob_eu)
print(suma_ue)

# Creación de capa vectorial ---------------------------------------------------
# Crea variable de capa vectorial con sistema de coordenadas en la memoria virtual
layer_2 = QgsVectorLayer("Point?crs=EPGS:4326", "capa_2", "memory")

# Crea variable con un campo de nombre "id" y de tipo cadena (string)
field = QgsField("id", QVariant.String)

# 2 formas de añadir ese campo a la capa creada, la de dataProvider no necesita activar edición
layer_2.dataProvider().addAttributes([field])
layer_2.addAttribute(field)

# Actualización de campos en la capa
layer_2.updateFields()

# Ver campos de la capa en formato lista
layer_2.fields().toList()

# Crea variable con un registro nuevo.
feature = QgsFeature()

# Establece la misma estructura de campos de la capa en el registro
feature.setFields(layer_2.fields())

# 3 formas distintas de ingresar un valor en un registro (de un campo)
feature.setAttributes(["1"])
feature.setAttribute(0, "2")
feature.setAttribute("id", "3")

# Crea variable con las coordenadas de un punto en X y Y
pt = QgsPointXY(1, 1)

# Crea variable con la geometría derivada del punto en XY
geom = QgsGeometry.fromPointXY(pt)

# Retorna la geometría en formato texto
geom.asWkt()

# Ingresa geometría en el registro creado
feature.setGeometry(geom)

# Ingresa el regsotro creado a la capa creada (por dataProvider)
layer_2.dataProvider().addFeatures([feature])

# Función para crear una capa con 50 registros aleatorios ----------------------
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