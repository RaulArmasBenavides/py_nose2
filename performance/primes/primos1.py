import cProfile

class Prime(object):
 
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.value = 0  # Adjusted to start from 1 for the logic in compute
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next item in iterator"""
        if self.count == self.n:
            raise StopIteration("end of iteration")
        return self.compute()
    
    def is_prime(self):
        """Whether current value is prime?"""
        if self.value < 2:
            return False
        if self.value == 2:
            return True  # 2 is prime
        if self.value % 2 == 0:
            return False  # Even numbers greater than 2 are not prime
        vroot = int(self.value ** 0.5) + 1
        for i in range(3, vroot, 2):  # Check only odd numbers
            if self.value % i == 0:
                return False
        return True
    
    def compute(self):
        """Compute next prime"""
        # Special case for the first prime number
        if self.count == 1:
           self.value = 1
 
        while True:
            self.value += 2
            if self.is_prime():
                self.count += 1
                break
        return self.value
    def print_primes(self):
        for p in Prime(5):
            print(p)


if __name__ == '__main__':
    for p in Prime(5):
        print(p)

    cProfile.run("list(Prime(1000))")