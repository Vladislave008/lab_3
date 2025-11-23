class Stack:
    def __init__(self, value: list| None = None):
        if value is None:
            value = []
        self.stack:list[tuple[int, int, int]] = []
        self.length: int = 0
        for elem in value:
            self.push(elem)

    def push(self, x: int) -> None:
        if self.is_empty():
            self.stack.append((x, x, x)) # value, current_min, current_max
        else:
            last_min = self.stack[-1][1]
            last_max = self.stack[-1][2]
            self.stack.append((x, min(last_min, x), max(last_max, x)))
        self.length += 1

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError('Stack is empty')
        self.length -= 1
        return self.stack.pop()[0]

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack[-1][0]

    def is_empty(self) -> bool:
        return self.length == 0

    def __len__(self) -> int:
        return self.length

    def min(self) -> int:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack[-1][1]

    def max(self) -> int:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack[-1][2]

    def print(self) -> None:
        m = [elem[0] for elem in self.stack]
        print(m)

class Queue:
    def __init__(self, value: list | None = None):
        if value is None:
            value = []
        self.in_stack = value.copy()
        self.out_stack:list[int] = []
        self.length = len(value)

    def enqueue(self, x: int) -> None:
        self.in_stack.append(x)
        self.length += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError('Queue is empty')
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        self.length -= 1
        return self.out_stack.pop()

    def front(self) -> int:
        if self.is_empty():
            raise ValueError('Queue is empty')
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def is_empty(self) -> bool:
        return self.length == 0

    def __len__(self) -> int:
        return self.length

    def print(self) -> None:
        print(self.out_stack[::-1] + self.in_stack)
