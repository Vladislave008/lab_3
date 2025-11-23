import pytest # type: ignore
from src.structures import Stack, Queue

class TestStack:
    def test_stack_basic_operations(self):
        stack = Stack()
        assert stack.is_empty()
        assert len(stack) == 0
        stack.push(1)
        assert not stack.is_empty()
        assert len(stack) == 1
        assert stack.peek() == 1
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3
        assert stack.peek() == 3
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_stack_min_max(self):
        stack = Stack()
        stack.push(5)
        assert stack.min() == 5
        assert stack.max() == 5
        stack.push(3)
        assert stack.min() == 3
        assert stack.max() == 5
        stack.push(7)
        assert stack.min() == 3
        assert stack.max() == 7
        stack.push(2)
        assert stack.min() == 2
        assert stack.max() == 7
        stack.pop()
        assert stack.min() == 3
        assert stack.max() == 7

    def test_stack_min_max_single_element(self):
        stack = Stack()
        stack.push(10)
        assert stack.min() == 10
        assert stack.max() == 10

    def test_stack_min_max_duplicates(self):
        stack = Stack()
        stack.push(5)
        stack.push(5)
        stack.push(3)
        stack.push(3)
        stack.push(7)
        stack.push(7)
        assert stack.min() == 3
        assert stack.max() == 7
        stack.pop()
        assert stack.min() == 3
        assert stack.max() == 7
        stack.pop()
        assert stack.min() == 3
        assert stack.max() == 5

    def test_stack_pop_empty(self):
        stack = Stack()
        with pytest.raises(ValueError, match="Stack is empty"):
            stack.pop()

    def test_stack_peek_empty(self):
        stack = Stack()
        with pytest.raises(ValueError, match="Stack is empty"):
            stack.peek()

    def test_stack_min_max_empty(self):
        stack = Stack()
        with pytest.raises(ValueError, match="Stack is empty"):
            stack.min()
        with pytest.raises(ValueError, match="Stack is empty"):
            stack.max()

    def test_stack_multiple_operations(self):
        stack = Stack()
        for i in range(100):
            stack.push(i)
        assert len(stack) == 100
        assert stack.min() == 0
        assert stack.max() == 99
        for i in range(99, -1, -1):
            assert stack.pop() == i

        assert stack.is_empty()


class TestQueue:
    def test_queue_basic_operations(self):
        queue = Queue()
        assert queue.is_empty()
        assert len(queue) == 0
        queue.enqueue(1)
        assert not queue.is_empty()
        assert len(queue) == 1
        assert queue.front() == 1

        queue.enqueue(2)
        queue.enqueue(3)
        assert len(queue) == 3
        assert queue.front() == 1
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()

    def test_queue_front_after_operations(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.front() == 1
        queue.enqueue(2)
        assert queue.front() == 1
        queue.dequeue()
        assert queue.front() == 2
        queue.enqueue(3)
        assert queue.front() == 2

    def test_queue_mixed_operations(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.is_empty()

    def test_queue_dequeue_empty(self):
        queue = Queue()
        with pytest.raises(ValueError, match="Queue is empty"):
            queue.dequeue()

    def test_queue_front_empty(self):
        queue = Queue()
        with pytest.raises(ValueError, match="Queue is empty"):
            queue.front()

    def test_queue_large_sequence(self):
        queue = Queue()
        for i in range(1000):
            queue.enqueue(i)
            assert len(queue) == i + 1
        for i in range(1000):
            assert queue.dequeue() == i

        assert queue.is_empty()

    def test_queue_two_stacks(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        queue.enqueue(4)
        queue.enqueue(5)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.is_empty()


def test_both_structures_together():
    stack = Stack()
    queue = Queue()
    for i in [5, 2, 8, 1, 9]:
        stack.push(i)
        queue.enqueue(i)
    assert stack.pop() == 9
    assert queue.dequeue() == 5
    assert stack.min() == 1
    assert stack.max() == 8
