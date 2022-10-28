# Script de procesamiento utilizando decoradores
# Importe de librerias
from qgis.core import edit
from qgis.processing import alg

# Configuración de descripción del script
@alg(name='renombrar_campo', label='Renombrar campo de capa vectorial',
     group='examplescripts', group_label='Example scripts')

# Configuración de entradas
@alg.input(type=alg.VECTOR_LAYER, name='INPUT', label='Capa vectorial de entrada')
@alg.input(type=alg.FIELD, name='INPUT_FIELD', label='Campo a renombrar', 
    parentLayerParameterName='INPUT')
@alg.input(type=alg.STRING, name='NAME_FIELD', label='Nuevo nombre de campo')

# Configuración de salidas
@alg.output(type=alg.VECTOR_LAYER, name='OUTPUT', label='Capa vectorial de salida')

# Función de procesamiento
def renombrar_campo(instance, parameters, context, feedback, inputs):
    """
    Renombra un campo de una capa vectorial.
    """
# Definición de variables según parámetros de entrada
    source = instance.parameterAsVectorLayer(parameters, 'INPUT', context)
    input_field = instance.parameterAsFields(parameters, 'INPUT_FIELD', context)[0]
    new_name = instance.parameterAsString(parameters, 'NAME_FIELD', context)

# Extracción del número de índice del campo a renombrar
    idx = source.fields().indexOf(input_field)
    
# Crear instancia de edición para modificar la capa vectorial
# Se requiere buscar el método que realiza la tarea (renameAttribute) en la capa vectorial
    with edit(source):
        source.renameAttribute(idx, new_name)
        
    return {'OUTPUT': source}
    
# Fin de código
    