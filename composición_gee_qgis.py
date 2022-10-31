import ee
from ee_plugin import Map

Map.setCenter(-85.5, 10.75, 15)
image = ee.ImageCollection("COPERNICUS/S2")\
    .filterBounds(Map.getCenter())\
    .filterMetadata ('CLOUDY_PIXEL_PERCENTAGE', 'Less_Than', 20)\
    .filterDate('2022-01-01', '2022-03-31').median()
    

Map.addLayer (image, {
     'max': 5000.0, 
     'min': 0.0,
     'gamma': 1.0, 
     'bands': ['B8','B4','B3']}, 
     'Capa Sentinel');