import pytest # type: ignore
from src.sorting import Sortings

class TestSortings:

    @pytest.fixture
    def s(self):
        return Sortings()

    @pytest.fixture
    def numbers(self):
        return [3, 1, 4, 1, 5, 9, 2, 6]

    @pytest.fixture
    def sorted_numbers(self):
        return [1, 1, 2, 3, 4, 5, 6, 9]

    @pytest.fixture
    def strings(self):
        return ['banana', 'apple', 'cherry', 'date']

    @pytest.fixture
    def students(self):
        return [
            {'name': 'Alice', 'age': 25, 'grade': 85},
            {'name': 'Bob', 'age': 20, 'grade': 92},
            {'name': 'Charlie', 'age': 23, 'grade': 78},
            {'name': 'Diana', 'age': 23, 'grade': 90}
        ]

    def test_empty_list(self, s):
        assert s.bubble_sort([]) == []
        assert s.quick_sort([]) == []
        assert s.counting_sort([]) == []
        assert s.radix_sort([]) == []
        assert s.heap_sort([]) == []
        assert s.bucket_sort([]) == []

    def test_single_element(self, s):
        assert s.bubble_sort([5]) == [5]
        assert s.quick_sort([5]) == [5]
        assert s.counting_sort([5]) == [5]
        assert s.radix_sort([5]) == [5]
        assert s.heap_sort([5]) == [5]
        assert s.bucket_sort([5]) == [5]

    def test_already_sorted(self, s):
        sorted_list = [1, 2, 3, 4, 5]
        assert s.bubble_sort(sorted_list) == sorted_list
        assert s.quick_sort(sorted_list) == sorted_list
        assert s.counting_sort(sorted_list) == sorted_list
        assert s.radix_sort(sorted_list) == sorted_list
        assert s.heap_sort(sorted_list) == sorted_list
        assert s.bucket_sort(sorted_list) == sorted_list

    def test_reverse_sorted(self, s):
        reverse_sorted = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert s.bubble_sort(reverse_sorted) == expected
        assert s.quick_sort(reverse_sorted) == expected
        assert s.counting_sort(reverse_sorted) == expected
        assert s.radix_sort(reverse_sorted) == expected
        assert s.heap_sort(reverse_sorted) == expected
        assert s.bucket_sort(reverse_sorted) == expected

    def test_key_with_numbers(self, s, numbers, sorted_numbers):
        def key_func(x):
            return x
        assert s.bubble_sort(numbers, key=key_func) == sorted_numbers
        assert s.quick_sort(numbers, key=key_func) == sorted_numbers
        assert s.heap_sort(numbers, key=key_func) == sorted_numbers

    def test_key_with_strings_length(self, s, strings):
        expected = ['date', 'apple', 'banana', 'cherry']
        result = s.bubble_sort(strings, key=len)
        assert result == expected

    def test_key_with_objects(self, s, students):
        result = s.quick_sort(students, key=lambda x: x['age'])
        ages = [s['age'] for s in result]
        assert ages == [20, 23, 23, 25]

    def test_key_with_complex_objects(self, s, students):
        result = s.heap_sort(students, key=lambda x: (x['age'], x['grade']))
        ages = [s['age'] for s in result]
        grades = [s['grade'] for s in result]
        assert ages == [20, 23, 23, 25]
        assert grades[1:3] == [78, 90]

    def test_cmp_reverse_numbers(self, s, numbers):
        def reverse_cmp(a: int, b: int) -> int:
            return b - a
        expected = [9, 6, 5, 4, 3, 2, 1, 1]
        assert s.bubble_sort(numbers, cmp=reverse_cmp) == expected
        assert s.quick_sort(numbers, cmp=reverse_cmp) == expected
        assert s.heap_sort(numbers, cmp=reverse_cmp) == expected

    def test_cmp_complex_logic(self, s, students):
        def age_then_grade_cmp(a: dict, b: dict) -> int:
            if a['age'] != b['age']:
                return a['age'] - b['age']
            return a['grade'] - b['grade']
        result = s.quick_sort(students, cmp=age_then_grade_cmp)
        ages = [s['age'] for s in result]
        grades = [s['grade'] for s in result]
        assert ages == [20, 23, 23, 25]
        assert grades[1:3] == [78, 90]

    def test_both_key_and_cmp_error(self, s, numbers):
        with pytest.raises(ValueError, match='Cannot use both "key" and "cmp" parameters'):
            s.bubble_sort(numbers, key=lambda x: x, cmp=lambda a, b: a - b)

    def test_counting_sort_cmp_error(self, s, numbers):
        with pytest.raises(ValueError, match='Counting_sort does not support cmp'):
            s.counting_sort(numbers, cmp=lambda a, b: a - b)

    def test_radix_sort_cmp_error(self, s, numbers):
        with pytest.raises(ValueError, match='Radix_sort does not support cmp'):
            s.radix_sort(numbers, cmp=lambda a, b: a - b)

    def test_counting_sort_non_int_key_error(self, s):
        students = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 20}
        ]
        with pytest.raises(ValueError, match='Counting sort requires integer keys'):
            s.counting_sort(students, key=lambda x: x['name'])

    def test_radix_sort_non_int_key_error(self, s, students):
        with pytest.raises(ValueError, match='Radix sort requires integer keys'):
            s.radix_sort(students, key=lambda x: x['name'])

    def test_counting_sort_negative_numbers(self, s):
        numbers = [-3, -1, -5, 0, 2, -2]
        expected = [-5, -3, -2, -1, 0, 2]
        assert s.counting_sort(numbers) == expected

    def test_radix_sort_large_numbers(self, s):
        numbers = [170, 45, 75, 90, 2, 802, 24, 66]
        expected = [2, 24, 45, 66, 75, 90, 170, 802]
        assert s.radix_sort(numbers) == expected

    def test_radix_sort_different_base(self, s):
        numbers = [15, 7, 3, 10, 12, 5]
        expected = [3, 5, 7, 10, 12, 15]
        assert s.radix_sort(numbers, base=2) == expected

    def test_bucket_sort_default_buckets(self, s, numbers, sorted_numbers):
        result = s.bucket_sort(numbers)
        assert result == sorted_numbers

    def test_bucket_sort_custom_buckets(self, s, numbers, sorted_numbers):
        result = s.bucket_sort(numbers, buckets=3)
        assert result == sorted_numbers

    def test_bucket_sort_with_key(self, s, students):
        result = s.bucket_sort(students, key=lambda x: x['age'], buckets=2)
        ages = [s['age'] for s in result]
        assert ages == [20, 23, 23, 25]

    def test_large_dataset(self, s):
        large_list = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        assert s.bubble_sort(large_list.copy()) == expected
        assert s.quick_sort(large_list.copy()) == expected
        assert s.counting_sort(large_list.copy()) == expected
        assert s.radix_sort(large_list.copy()) == expected
        assert s.heap_sort(large_list.copy()) == expected
        assert s.bucket_sort(large_list.copy()) == expected

    def test_duplicate_elements(self, s):
        numbers = [5, 2, 8, 2, 5, 1, 8]
        expected = [1, 2, 2, 5, 5, 8, 8]
        assert s.quick_sort(numbers) == expected
        assert s.counting_sort(numbers) == expected

    def test_all_same_elements(self, s):
        numbers = [5, 5, 5, 5, 5]
        assert s.bubble_sort(numbers) == numbers
        assert s.quick_sort(numbers) == numbers
        assert s.counting_sort(numbers) == numbers

    def test_floats_with_bucket_sort(self, s):
        floats = [0.3, 0.1, 0.4, 0.1, 0.5]
        expected = [0.1, 0.1, 0.3, 0.4, 0.5]
        result = s.bucket_sort(floats, buckets=5)
        assert result == expected

    def test_apply_key_no_key(self, s):
        result = s.apply_key([1, 2, 3])
        assert result == [(1, 1), (2, 2), (3, 3)]

    def test_apply_key_with_key(self, s):
        result = s.apply_key([1, 2, 3], key=lambda x: x * 2)
        assert result == [(2, 1), (4, 2), (6, 3)]

    def test_extract_original(self, s):
        paired = [(1, 'a'), (2, 'b'), (3, 'c')]
        result = s.extract_original(paired)
        assert result == ['a', 'b', 'c']
