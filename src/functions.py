from functools import lru_cache

class Functions():

    def factorial(self, n: int) -> int:
        '''Вычисляет факториал числа n итеративным методом'''
        if n < 0 or not isinstance(n, int):
            raise ValueError('Factorial argument must be non-negative int')
        if n == 0 or n == 1:
            return 1
        res = 1
        for i in range(1,n+1):
            res *= i
        return res

    @lru_cache(maxsize=None)
    def factorial_recursive(self, n: int) -> int:
        '''Вычисляет факториал числа n рекурсивным методом'''
        if n < 0 or not isinstance(n, int):
            raise ValueError('Factorial argument must be non-negative int')
        if n == 0 or n == 1:
            return 1
        return n*self.factorial_recursive(n-1)

    def fibo(self, n: int) -> int:
        '''Вычисляет n-е число Фибоначчи итеративным методом'''
        if n < 0 or not isinstance(n, int):
            raise ValueError('Fibonacci argument must be non-negative int')
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a = 1 # n-2
        b = 1 # n-1
        for i in range(3,n+1):
            a,b = b, a+b
        return b

    @lru_cache(maxsize=None)
    def fibo_recursive(self, n: int) -> int:
        '''Вычисляет n-е число Фибоначчи рекурсивным методом'''
        if n < 0 or not isinstance(n, int):
            raise ValueError('Fibonacci argument must be non-negative int')
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fibo_recursive(n-1) + self.fibo_recursive(n-2)
