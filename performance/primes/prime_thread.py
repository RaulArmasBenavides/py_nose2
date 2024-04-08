
# from multiprocessing import Queue
from queue import Queue
import threading
import time


def is_prime(n):
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
          print(n,'is not prime')
          return False
        print(n,'is prime')
        return True
    
class PrimeChecker(threading.Thread):
    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        threading.Thread.__init__(self)

    def run(self):
        while self.flag:
            try:
                n = self.queue.get(timeout=1)
                is_prime(n)
            except Exception as e:
                print(e)
                raise

if __name__ == '__main__':
    start_time = time.time()
    numbers = [1297337, 1116281, 104395303, 472882027, 533000389,
    817504243, 982451653, 112272535095293, 115280095190773,
    1099726899285419]*100
    q = Queue(1000)
    for n in numbers:
     q.put(n)
    threads = []
    for i in range(4):
        t = PrimeChecker(q)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")