from random import choice
import time
import concurrent.futures
import timeit
# Simula la verificación de una transacción
def verificar_transaccion(transaccion):
    resultado = choice(['Aprobada', 'Rechazada', 'Revisión manual'])
    #print(f"Transacción {transaccion['id']}: {resultado}")
    return resultado

# Lista de transacciones de ejemplo
transacciones = [{'id': i, 'usuario': f'usuario_{i}', 'monto': i*100} for i in range(1, 123456)]

def main():
    start_time = time.time()
    resultados = [verificar_transaccion(t) for t in transacciones]
    end_time = time.time()
    # print("Verificación completada para todas las transacciones sin paralelismo. Tiempo de ejecución:", end_time - start_time)


def main2():
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultados = list(executor.map(verificar_transaccion, transacciones))
    end_time = time.time()
    # print("Verificación completada para todas las transacciones con paralelismo. Tiempo de ejecución (paralelo):", end_time - start_time)

if __name__ == "__main__":
    # Nota: timeit desactiva la salida estándar por defecto, así que no verás los prints al usar timeit
    secuencial_time = timeit.timeit('main()', globals=globals(), number=1)
    paralelo_time = timeit.timeit('main2()', globals=globals(), number=1)
    print(f"Tiempo de ejecución secuencial: {secuencial_time} segundos.")
    print(f"Tiempo de ejecución en paralelo: {paralelo_time} segundos.")