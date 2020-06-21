from functools import lru_cache

@lru_cache(maxsize=64)
def fib(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    return fib(t-1) + fib(t-2)

n = int(input())

for i in range(n):
    t = int(input())
    if (0 <= t <= 60):
        print("Fib({}) = {}".format(
            t,
            fib(t)
        ))