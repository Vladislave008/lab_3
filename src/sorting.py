import random
from typing import TypeVar, Callable, Any, Optional
import functools

T = TypeVar('T')
class Sortings():

    def handle_cmp(self, a: list[T], key:Optional[Callable[[T], Any]] | None, cmp: Callable[[T, T], int] | None):
        '''Вспомогательный метод для преобразования компаратора в ключ'''
        if key is not None and cmp is not None:
            raise ValueError('Cannot use both "key" and "cmp" parameters at the same time')
        if cmp is not None:
            key = functools.cmp_to_key(cmp)
        return self.apply_key(a, key)

    def apply_key(self, arr: list[T], key:Optional[Callable[[T], Any]] = None) -> list[tuple]:
        '''Вспомогательный метод для применения ключа'''
        if key is None:
            return [(elem, elem) for elem in arr]
        return [(key(elem), elem) for elem in arr]

    def extract_original(self, paired_list: list[tuple]) -> list[T]:
        '''Метод для извлечения исходных элементов из пар'''
        return [orig_val for key_val, orig_val in paired_list]

    def bubble_sort(self, a: list[T], key:Optional[Callable[[T], Any]] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        if not a:
            return []
        arr = self.handle_cmp(a, key, cmp)
        was_changed = 1
        while was_changed:
            was_changed = 0
            for i in range(len(arr)-1):
                if arr[i][0] > arr[i+1][0]:
                    was_changed = 1
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        return self.extract_original(arr)

    def quick_sort(self, a: list[T], key:Optional[Callable[[T], Any]] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        if len(a) <= 1:
            return a
        else:
            arr = self.handle_cmp(a, key, cmp)
            less = []
            equal = []
            more = []
            pivot = arr[random.randint(0, len(arr)-1)][0]
            for key_val, orig_val in arr:
                if key_val < pivot:
                    less.append(orig_val)
                elif key_val > pivot:
                    more.append(orig_val)
                else:
                    equal.append(orig_val)
            return self.quick_sort(less, key, cmp) + equal + self.quick_sort(more, key, cmp)

    def counting_sort(self, a: list[T], key: Callable[[T], int] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        if cmp is not None:
            raise ValueError('Counting_sort does not support cmp, use key instead')
        if not a:
            return []

        paired = self.apply_key(a, key)
        keys = [key_val for key_val, orig_val in paired]
        if keys and not all(isinstance(k, int) for k in keys):
            raise ValueError('Counting sort requires integer keys')
        min_elem = min(keys)
        max_elem = max(keys)
        counter = [0 for i in range(min_elem, max_elem + 1)]
        for key_val in keys:
            counter[key_val-min_elem] += 1
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        result = [0] * len(a) # type:ignore
        for i in range(len(paired)-1, -1, -1):
            key_val, orig_val = paired[i]
            pos = counter[key_val - min_elem] - 1
            result[pos] = orig_val
            counter[key_val - min_elem] -= 1
        return result

    def counting_sort_for_radix(self, paired: list[tuple[int, T]], exp: int) -> list[tuple[int, T]]:
        keys = [key_val for key_val, orig_val in paired]
        n = len(keys)
        res = [0] * n
        counter = [0] * 10 # для каждой цифры
        for i in range(n): # подсчет вхождений цифр в текущем разряде
            index = (keys[i] // exp) % 10
            counter[index] += 1
        for i in range(1, 10): # накопительная сумма
            counter[i] += counter[i - 1]
        for i in range(n-1,-1,-1):
            index = (keys[i] // exp) % 10
            res[counter[index] - 1] = paired[i]
            counter[index] -= 1
        return res

    def radix_sort(self, a: list[T], key: Callable[[T], int] | None = None, cmp: Callable[[T, T], int] | None = None, base: int = 10) -> list[T]:
        if cmp is not None:
            raise ValueError('Radix_sort does not support cmp, use key instead')
        if not a:
            return []
        paired = self.apply_key(a, key)
        keys = [key_val for key_val, orig_val in paired]
        if not all(isinstance(k, int) for k in keys):
            raise ValueError('Radix sort requires integer keys')
        digits = len(str(max(keys)))
        div = base
        for i in range(digits):
            paired = self.counting_sort_for_radix(paired, div**i)
        return self.extract_original(paired)

    def bucket_sort(self, a: list[T], key:Optional[Callable[[T], Any]] | None = None, cmp: Callable[[T, T], int] | None = None, buckets: int | None = None) -> list[T]:
        if not a:
            return []
        if cmp is not None:
            raise ValueError('Bucket_sort does not support cmp, use key instead')
        paired = self.apply_key(a, key)
        keys = [key_val for key_val, orig_val in paired]
        min_elem = min(keys)
        max_elem = max(keys)
        if buckets is None:
            buckets = len(keys)
        bucket_list: list[list[tuple[Any, T]]] = [[] for _ in range(buckets)]
        for key_val, orig_val in paired:
            index = int((key_val - min_elem) / (max_elem - min_elem + 1e-10) * buckets)
            index = min(index, buckets - 1)
            bucket_list[index].append(orig_val)
        for i in range(len(bucket_list)):
            bucket_list[i] = self.quick_sort(bucket_list[i], key, cmp)
        result = []
        for bucket in bucket_list:
            result.extend(bucket)
        return result

    def heapify(self, keys: list, originals: list, n: int, i: int):
        largest = i
        left = 2 * i + 1   # левый потомок
        right = 2 * i + 2  # правый потомок
        # находим наибольший среди корня и потомков
        if left < n and keys[left] > keys[largest]:
            largest = left
        if right < n and keys[right] > keys[largest]:
            largest = right
        if largest != i:
            # меняем местами и ключи, и исходные элементы
            keys[i], keys[largest] = keys[largest], keys[i]
            originals[i], originals[largest] = originals[largest], originals[i]
            self.heapify(keys, originals, n, largest)

    def heap_sort(self, a: list[T], key:Optional[Callable[[T], Any]] | None = None, cmp: Callable[[T, T], int] | None = None) -> list[T]:
        if len(a) <= 1:
            return a
        paired = self.handle_cmp(a, key, cmp)
        keys = [key_val for key_val, orig_val in paired]
        origs = [orig_val for key_val, orig_val in paired]
        n = len(paired)
        # получаем корректную кучу (идем по дереву снизу)
        for i in range(n // 2 - 1, -1, -1): # n // 2 - 1 является последним нелистовым узлом
            self.heapify(keys, origs, n, i)
        for i in range(n-1, 0, -1):
            # перемещаем текущий корень в конец
            keys[0], keys[i] = keys[i], keys[0]
            origs[0], origs[i] = origs[i], origs[0]
            # восстанавливаем max-heap для уменьшенной кучи
            self.heapify(keys, origs, i, 0)
        return origs
