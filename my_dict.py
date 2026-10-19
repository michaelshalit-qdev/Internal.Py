from my_list import List



class Entry:
    def __init__(self, key: object, value: object) -> None:
        #store key and value
        self.key = key
        self.value = value
        
class Dict:
    def __init__(self) -> None:
        # store our entries
        self._items = List()

    def __len__(self) -> int:
        return len(self._items)
        
    def __setitem__(self, key: object, value: object) -> None:
        # check if key already exists
        for item in self._items:
            if item.key == key:
                item.value = value

        # add new key and value
        self._items.append(Entry(key, value))

    def __getitem__(self, key: object) -> object:
        # search for key
        for item in self._items:
            if item.key == key:
                return item.value

        # key was not found
        raise KeyError(key)