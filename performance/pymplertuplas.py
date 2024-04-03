from pympler import asizeof
from pympler import muppy, summary
# Vamos a generar una lista de tuplas, donde cada tupla contiene números de 0 a 999
big_list_of_tuples = [(i, i+1, i+2) for i in range(1000)]

# Ahora usamos asizeof.asizeof() para obtener el tamaño de la lista en bytes
size_in_bytes = asizeof.asizeof(big_list_of_tuples)
print(f"El tamaño de big_list_of_tuples es: {size_in_bytes} bytes")

# Obtenemos todos los objetos actualmente en memoria
all_objects = muppy.get_objects()
print(f"Número total de objetos en memoria: {len(all_objects)}")

# Imprimimos un resumen del uso de memoria
sum1 = summary.summarize(all_objects)
summary.print_(sum1)

# Para ver el efecto de la creación de la lista grande, vamos a generar otra
another_big_list = [i for i in range(10000)]

# Imprimimos la diferencia en memoria después de crear la nueva lista grande
all_objects = muppy.get_objects()
sum2 = summary.summarize(all_objects)
summary.print_(sum2)

# Imprimimos la diferencia entre los dos resúmenes para ver el cambio en uso de memoria
diff = summary.get_diff(sum1, sum2)
print("Diferencia después de crear another_big_list:")
summary.print_(diff)