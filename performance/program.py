import random
from time import perf_counter as timer_func
from contextlib import contextmanager
def common_items(seq1, seq2):
    """ Find common items between two sequences """
    common = []
    for item in seq1:
     if item in seq2:
        common.append(item)
        return common
     

@contextmanager
def timer():
  try:
    start = timer_func()
    yield
  except Exception as e:
    print(e)
    raise
  finally:
    end = timer_func()
    print('Time spent=>',1000.0 * (end - start),'ms.')

def test(n):
    """ Generate test data for numerical lists given input size
    """
    a1=random.sample(range(0, 2*n), n)
    a2=random.sample(range(0, 2*n), n)
    return a1, a2
def test(n, func):
    """ Generate test data and perform test on a given function
    """
    a1=random.sample(range(0, 2*n), n)
    a2=random.sample(range(0, 2*n), n)
    with timer() as t:
     result = func(a1, a2)

test(100, common_items)
test(200, common_items)
test(400, common_items)