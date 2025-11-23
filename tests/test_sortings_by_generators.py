import pytest # type: ignore
from src.sorting import Sortings
from tests.testcase_generation import TestCaseGenerator

class TestSortings:

    def setup_method(self):
        self.sortings = Sortings()
        self.test_seed = 42

    def run_sort_test(self, sort_func, test_data):
        expected = sorted(test_data)
        result = sort_func(test_data)
        assert result == expected

    def run_sort_test_with_key(self, sort_func, test_data, key_func):
        expected = sorted(test_data, key=key_func)
        result = sort_func(test_data, key=key_func)
        assert result == expected

    def test_bubble_sort_basic(self):
        test_cases = [
            TestCaseGenerator.rand_int_array(100, 0, 1000, seed=self.test_seed),
            TestCaseGenerator.nearly_sorted(50, 5, seed=self.test_seed),
            TestCaseGenerator.many_duplicates(100, 5, seed=self.test_seed),
            TestCaseGenerator.reverse_sorted(100),
            [1],
            []
        ]
        for data in test_cases:
            self.run_sort_test(self.sortings.bubble_sort, data)

    def test_bubble_sort_with_key(self):
        data = TestCaseGenerator.rand_int_array(50, 1, 100, seed=self.test_seed)
        self.run_sort_test_with_key(
            self.sortings.bubble_sort,
            [-x for x in data],
            abs
        )
        string_data = [f'item_{x}' for x in data]
        self.run_sort_test_with_key(
            self.sortings.bubble_sort,
            string_data,
            lambda x: int(x.split('_')[1])
        )

    def test_quick_sort_basic(self):
        test_cases = [
            TestCaseGenerator.rand_int_array(200, 0, 1000, seed=self.test_seed),
            TestCaseGenerator.nearly_sorted(100, 10, seed=self.test_seed),
            TestCaseGenerator.many_duplicates(150, 3, seed=self.test_seed),
            TestCaseGenerator.reverse_sorted(100),
            [5, 5, 5, 5]]
        for data in test_cases:
            self.run_sort_test(self.sortings.quick_sort, data)

    def test_quick_sort_edge_cases(self):
        assert self.sortings.quick_sort([]) == []
        assert self.sortings.quick_sort([42]) == [42]
        assert self.sortings.quick_sort([2, 1]) == [1, 2]

    def test_counting_sort_basic(self):
        test_cases = [
            TestCaseGenerator.rand_int_array(100, 0, 50, seed=self.test_seed),
            TestCaseGenerator.many_duplicates(100, 10, seed=self.test_seed),
            list(range(50)),
            TestCaseGenerator.reverse_sorted(50)
        ]
        for data in test_cases:
            self.run_sort_test(self.sortings.counting_sort, data)

    def test_counting_sort_with_key(self):
        data = TestCaseGenerator.rand_int_array(50, 1, 100, seed=self.test_seed)
        self.run_sort_test_with_key(
            self.sortings.counting_sort,
            data,
            lambda x: x % 50
        )

    def test_counting_sort_validation(self):
        with pytest.raises(ValueError, match='Counting sort requires integer keys'):
            self.sortings.counting_sort([1.5, 2.3, 0.7])
        with pytest.raises(ValueError, match='Counting_sort does not support cmp'):
            self.sortings.counting_sort([1, 2, 3], cmp=lambda a, b: a - b)

    def test_radix_sort_basic(self):
        test_cases = [
            TestCaseGenerator.rand_int_array(100, 0, 1000, seed=self.test_seed),
            [170, 45, 75, 90, 2, 802, 2, 66],
            list(range(100)),
            [999, 100, 10, 1, 0]
        ]
        for data in test_cases:
            self.run_sort_test(self.sortings.radix_sort, data)

    def test_radix_sort_with_key(self):
        data = [('a', 123), ('b', 45), ('c', 678), ('d', 9)]
        self.run_sort_test_with_key(
            self.sortings.radix_sort,
            data,
            lambda x: x[1]
        )

    def test_radix_sort_validation(self):
        with pytest.raises(ValueError, match='Radix sort requires integer keys'):
            self.sortings.radix_sort([1.5, 2.3])
        with pytest.raises(ValueError, match='Radix_sort does not support cmp'):
            self.sortings.radix_sort([1, 2, 3], cmp=lambda a, b: a - b)

    def test_bucket_sort_basic(self):
        float_data = TestCaseGenerator.rand_float_array(100, 0.0, 1.0, seed=self.test_seed)
        self.run_sort_test(self.sortings.bucket_sort, float_data)
        int_data = TestCaseGenerator.rand_int_array(100, 0, 100, seed=self.test_seed)
        self.run_sort_test(self.sortings.bucket_sort, int_data)

    def test_bucket_sort_with_buckets_param(self):
        data = TestCaseGenerator.rand_float_array(50, 0.0, 1.0, seed=self.test_seed)
        for buckets in [5, 10, 20, 50]:
            result = self.sortings.bucket_sort(data, buckets=buckets)
            expected = sorted(data)
            assert result == expected

    def test_bucket_sort_validation(self):
        with pytest.raises(ValueError, match='Bucket_sort does not support cmp'):
            self.sortings.bucket_sort([1, 2, 3], cmp=lambda a, b: a - b)

    def test_heap_sort_basic(self):
        test_cases = [
            TestCaseGenerator.rand_int_array(150, 0, 500, seed=self.test_seed),
            TestCaseGenerator.nearly_sorted(80, 8, seed=self.test_seed),
            TestCaseGenerator.many_duplicates(100, 4, seed=self.test_seed),
            TestCaseGenerator.reverse_sorted(100)
        ]
        for data in test_cases:
            self.run_sort_test(self.sortings.heap_sort, data)

    def test_heap_sort_with_key(self):
        data = TestCaseGenerator.rand_int_array(50, 1, 100, seed=self.test_seed)
        self.run_sort_test_with_key(
            self.sortings.heap_sort,
            [-x for x in data],
            abs
        )

    def test_large_datasets(self):
        large_datasets = [
            TestCaseGenerator.rand_int_array(1000, 1, 10000, seed=self.test_seed),
            TestCaseGenerator.many_duplicates(1000, 50, seed=self.test_seed),
            TestCaseGenerator.nearly_sorted(1000, 20, seed=self.test_seed),
        ]
        for data in large_datasets:
            self.run_sort_test(self.sortings.quick_sort, data)
            self.run_sort_test(self.sortings.heap_sort, data)
            self.run_sort_test(self.sortings.bubble_sort, data)
            self.run_sort_test(self.sortings.counting_sort, data)
            self.run_sort_test(self.sortings.radix_sort, data)
            self.run_sort_test(self.sortings.bucket_sort, data)

    def test_with_cmp(self):
        data = TestCaseGenerator.rand_int_array(30, 1, 100, seed=self.test_seed)
        def reverse_cmp(a, b):
            return b - a
        for sorter in [self.sortings.bubble_sort, self.sortings.quick_sort, self.sortings.heap_sort]:
            result = sorter(data, cmp=reverse_cmp)
            expected = sorted(data, reverse=True)
            assert result == expected

    def test_cmp_key_conflict(self):
        data = [1, 2, 3]
        with pytest.raises(ValueError, match='Cannot use both "key" and "cmp" parameters'):
            self.sortings.bubble_sort(data, key=lambda x: x, cmp=lambda a, b: a - b)
