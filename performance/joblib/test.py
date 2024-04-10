from joblib import dump, load
import numpy as np

# Creando un objeto grande, por ejemplo, una gran matriz NumPy
data = np.arange(1000000).reshape(1000, 1000)

# Guardando el objeto a un archivo
dump(data, 'large_array.joblib')

# Cargando el objeto desde un archivo
loaded_data = load('large_array.joblib')

print(loaded_data.shape)  # Debería imprimir (1000, 1000)
