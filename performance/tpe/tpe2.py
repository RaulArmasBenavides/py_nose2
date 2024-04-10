from random import choice
import concurrent.futures
import timeit

# Simula la verificación de una transacción
def verificar_transaccion(transaccion):
     # Simula la complejidad de la tarea con un cálculo que consume CPU
    suma = 0
    for i in range(10000):
        suma += (i * transaccion['monto']) % (transaccion['id'] + 1)
    
    resultado = choice(['Aprobada', 'Rechazada', 'Revisión manual'])
    return resultado

# Lista de transacciones de ejemplo
transacciones = [{'id': i, 'usuario': f'usuario_{i}', 'monto': i*100} for i in range(1, 100)]

def main():
    # Esta función permanece igual, ejecutando secuencialmente
    resultados = [verificar_transaccion(t) for t in transacciones]

def main2():
    # Modificada para usar ProcessPoolExecutor en lugar de ThreadPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        resultados = list(executor.map(verificar_transaccion, transacciones))

if __name__ == "__main__":
    secuencial_time = timeit.timeit('main()', globals=globals(), number=1)
    paralelo_time = timeit.timeit('main2()', globals=globals(), number=1)
    print(f"Tiempo de ejecución secuencial: {secuencial_time} segundos.")
    print(f"Tiempo de ejecución en paralelo (procesos): {paralelo_time} segundos.")
