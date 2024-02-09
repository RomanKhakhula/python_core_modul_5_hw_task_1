# Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Outer function wo args. Return fnction fibonacci(n: int)"""
    cache = {}
    def fibonacci(n: int) -> int:
        """Calculate elements of Fibonacci sequence. F(n) = F(n - 1) + (n - 2). Adds and keeps in cache calculated elements."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache.keys():
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

# Check results
# fib_el = caching_fibonacci()
# print(fib_el(10))
# print(fib_el(15))

