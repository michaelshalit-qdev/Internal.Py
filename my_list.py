
from typing import Iterable, Iterator , Generator


class Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next = None


class List:
    def __init__(self, iteration: Iterable[object] | None = None) -> None:
        self._head = None
        self._tail = None
        self.length = 0

        if iteration is not None:
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
    
    def _normalize_index(self, index: int, for_insert: bool = False) -> int:
        # check index type
        if not isinstance(index, int):
            raise TypeError("list indices must be integers")

        # negative index
        if index < 0:
            index += self.length

        if for_insert:
            # limit index to valid position
            if index < 0:
                index = 0
            if index > self.length:
                index = self.length
        else:
            # check index range
            if index < 0 or index >= self.length:
                raise IndexError("list index out of range")

        return index
    
    def _node_at(self, index: int) -> Node:
        # check index type
        index = self._normalize_index(index)

        current = self._head
        current_index = 0

        # find node
        while current_index < index:
            assert current is not None
            current = current.next
            current_index += 1

        assert current is not None
        return current


    def __getitem__(self, index: int) -> object:
        return self._node_at(index).value

    def __setitem__(self, index: int, value: object) -> None:
        self._node_at(index).value = value

    def __iter__(self) -> Generator[object, None, None]:
        current = self._head

        # go through nodes
        while current is not None:
            yield current.value
            current = current.next

    def insert(self, index: int, value: object) -> None:
        # normalise index
        index = self._normalize_index(index, for_insert=True)

        # add at end
        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)

        if index == 0:
            # add at beginning
            new_node.next = self._head
            self._head = new_node
        else:
            # find previous node
            previous = self._node_at(index - 1)
            new_node.next = previous.next
            previous.next = new_node

        self.length += 1
        

    def remove(self, value: object) -> None:
        # start from first node
        current = self._head
        previous = None

        while current is not None:
            # check if value matches
            if current.value is value:
                if previous is None:
                    # remove first node
                    self._head = current.next
                else:
                    # skip current node
                    previous.next = current.next

                self.length -= 1
                return

            previous = current
            current = current.next

        raise ValueError("value not found")
        
    # def pop(self, index: int = -1) -> object:
        # check if list is empty
        # if self.length == 0:
            # raise IndexError("pop from empty list")
          # get index
        # index = self._normalize_index(index)

        # current = self._head
        # previous = None
        # current_index = 0

        # find position
        # while current_index < index:
            # previous = current
            # current = current.next
            # current_index += 1