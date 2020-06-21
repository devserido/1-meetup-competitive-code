from functools import lru_cache

@lru_cache(maxsize=64)
def fib(t):
    if t == 0 or t == 1:
        return t
    return fib(t-1) + fib(t-2)

n = int(input())

for _ in range(n):
    t = int(input())
    if (0 <= t <= 60):
        print("Fib({}) = {}".format(t, fib(t)))
        