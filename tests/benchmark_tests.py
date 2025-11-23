import time
from typing import Callable
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sorting import Sortings
from testcase_generation import TestCaseGenerator

def timeit_once(func: Callable, *args, **kwargs) -> float:
    '''Измеряет время выполнения функции один раз'''
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    '''
    Бенчмарк сортировок на разных наборах данных
    Args:
        arrays: словарь {list_name: list}
        algos: словарь {algo_name: algo_func}
    Returns:
        Словарь {algo_name: {list_name: time}}
    '''
    results: dict[str, float] = {}
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        for array_name, array in arrays.items():
            test_array = array.copy()
            time_taken = timeit_once(algo_func, test_array)
            results[algo_name][array_name] = time_taken
    return results


arrays = {
    "random_1000": TestCaseGenerator.rand_int_array(1000, 1, 10000, seed=42),
    "sorted_1000": list(range(1000)),
    "reversed_1000": TestCaseGenerator.reverse_sorted(1000),
    "nearly_sorted_1000": TestCaseGenerator.nearly_sorted(1000, 50, seed=42),
    "many_duplicates_1000": TestCaseGenerator.many_duplicates(1000, 10, seed=42),
}

sortings = Sortings()
algos = {
    "bubble_sort": sortings.bubble_sort,
    "quick_sort": sortings.quick_sort,
    "heap_sort": sortings.heap_sort,
    "counting_sort": sortings.counting_sort,
    "radix_sort": sortings.radix_sort,
    "bucket_sort": sortings.bucket_sort,
    "builtin_sorted": sorted,
}

results: dict[str, float] = benchmark_sorts(arrays, algos)

print("Time spent:")
for algo_name, times in results.items():
    print(f"\n{algo_name}:")
    for array_name, time_taken in times.items():
        print(f"  {array_name}: {time_taken:.6f}")
