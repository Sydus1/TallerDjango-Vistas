from ..models import Measurement

# Consultar la lista de todas las medidas
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


# Consultar una medida por su id
def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement


# Crear una medida
def create_measurement(mea):
    measurement = Measurement(variable=mea["variable"], value=mea["value"], unit=mea["unit"], place=mea["place"], dateTime=mea["dateTime"])
    measurement.save()
    return measurement


# Cambiar una medida con si id
def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.name = new_mea["name"]
    measurement.save()
    return measurement


# Eliminar un medida por su identificador
def delete_measurement(mea_pk):
    measurement = get_measurement(mea_pk)
    Measurement.delete(measurement)
