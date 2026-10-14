
from typing import Iterable, Iterator


class Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None


class List:
    def __init__(self, iteration: Iterable[object] | None = None) -> None:
        self._head = None
        self._tail = None
        self.length = 0

        if iteration is None:
            pass
        else:
            for value in iteration:
                self.append(value)

    def __len__(self) -> int:
        return self.length

    def append(self, value: object) -> None:
        # add new node
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self.length += 1

    def extend(self, iteration: Iterable[object]) -> None:
        # add multiple values
        for value in iteration:
            self.append(value)

    def _node_at(self, index: int) -> Node:
        # check index type
        if not isinstance(index, int):
            raise TypeError("list indices must be integers")

        # negative index
        if index < 0:
            index += self.length

        # check index range
        if index < 0 or index >= self.length:
            raise IndexError("list index out of range")

        current = self._head
        current_index = 0

        # find node
        while current_index < index:
            current = current.next
            current_index += 1

        return current

    def __getitem__(self, index: int) -> object:
        return self._node_at(index).value

    def __setitem__(self, index: int, value: object) -> None:
        self._node_at(index).value = value

    def __iter__(self) -> Iterator[object]:
        current = self._head

        while current is not None:
            yield current.value
            current = current.next

    def insert(self, index: int, value: object) -> None:
        # add value at index
        new_node = Node(value)

        if index < 0:
            index = 0

        if index <= 0:
            new_node.next = self._head
            self._head = new_node

            if self._tail is None:
                self._tail = new_node

            return

        if index >= self.length:
            self.append(value)
            return

        # find previous node
        previous = self._node_at(index - 1)

        new_node.next = previous.next
        previous.next = new_node

        self.length += 1