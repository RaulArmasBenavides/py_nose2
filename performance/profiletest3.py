# mem_profile_example.py
@profile
def squares(n):
    return [x*x for x in range(1, n+1)]
squares(100)