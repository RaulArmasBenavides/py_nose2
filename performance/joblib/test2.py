from math import sqrt
from joblib import Parallel, delayed

# Una función simple que queremos ejecutar en paralelo
def process_input(i):
    return sqrt(i)

# Lista de entradas sobre las cuales queremos aplicar la función
inputs = range(10)

# Usando joblib para ejecutar la función en paralelo sobre las entradas
results = Parallel(n_jobs=2)(delayed(process_input)(i) for i in inputs)

print(results)  # Debería imprimir los resultados de aplicar sqrt a los números de 0 a 9