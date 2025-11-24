import random

class TestCaseGeneratorInteractive:

    @staticmethod
    def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
        '''
        Генерирует массив случайных целых чисел
        Args:
            n: количество элементов
            lo: нижняя граница (включительно)
            hi: верхняя граница (включительно)
            distinct: если True, все элементы уникальны
            seed: seed для генератора случайных чисел
        '''
        n = int(n)
        lo = int(lo)
        hi = int(hi)
        distinct = bool(distinct)
        if seed == 'None':
            seed = None
        elif seed is not None: 
            seed = int(seed)
        if seed is not None:
            random.seed(seed)
        if distinct:
            if hi - lo + 1 < n:
                raise ValueError('Unable to generate unique values: the interval is too small')
            return random.sample(range(lo, hi + 1), n)
        else:
            return [random.randint(lo, hi) for _ in range(n)]

    @staticmethod
    def nearly_sorted(n: int, swaps: int, seed=None) -> list[int]:
        '''
        Генерирует почти отсортированный массив
        Args:
            n: количество элементов
            swaps: количество пар элементов для обмена
            seed: seed для генератора случайных чисел
        '''
        n = int(n)
        swaps = int(swaps)
        if seed == 'None':
            seed = None
        elif seed is not None: 
            seed = int(seed)
        if seed is not None:
            random.seed(seed)
        arr = list(range(n))
        for _ in range(swaps):
            i, j = random.sample(range(n), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    @staticmethod
    def many_duplicates(n: int, k_unique=5, seed=None) -> list[int]:
        '''
        Генерирует массив с большим количеством дубликатов
        Args:
            n: количество элементов
            k_unique: количество уникальных значений
            seed: seed для генератора случайных чисел
        '''
        n = int(n)
        k_unique = int(k_unique)
        if seed == 'None':
            seed = None
        elif seed is not None: 
            seed = int(seed)
        if seed is not None:
            random.seed(seed)
        if k_unique <= 0:
            raise ValueError('k_unique must be positive')
        unique_values = list(range(k_unique))
        return [random.choice(unique_values) for _ in range(n)]

    @staticmethod
    def reverse_sorted(n: int) -> list[int]:
        n = int(n)
        '''
        Генерирует обратно отсортированный массив
        Args:
            n: количество элементов
        '''
        return list(range(n-1, -1, -1))

    @staticmethod
    def rand_float_array(n: int, lo=0.0, hi=1.0, seed=None) -> list[float]:
        '''
        Генерирует массив случайных чисел с плавающей точкой
        Args:
            n: количество элементов
            lo: нижняя граница (включительно)
            hi: верхняя граница (включительно)
            seed: seed для генератора случайных чисел
        '''
        n = int(n)
        lo = float(lo)
        hi = float(hi)
        if seed == 'None':
            seed = None
        elif seed is not None: 
            seed = int(seed)
        if seed is not None:
            random.seed(seed)
        return [random.uniform(lo, hi) for _ in range(n)]