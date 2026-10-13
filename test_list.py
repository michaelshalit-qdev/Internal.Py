# ruff: noqa: D103, ANN201

from itertools import chain

import pytest

from my_list import List

LIST = list
# LIST = List


def test_create_object_no_args():
    my_list = LIST()
    assert len(my_list) == 0


def test_create_object_from_iterable():
    num_elements = 3
    my_list2 = LIST(range(num_elements))
    assert len(my_list2) == num_elements


def test_create_object_from_big_iterable():
    num_elements = 10_000
    my_list2 = LIST(range(num_elements))
    assert len(my_list2) == num_elements


def test_len():
    input_string = "hello world!"
    my_list2 = LIST(input_string)
    assert len(my_list2) == len(input_string)


def test_set_in_the_middle():
    my_list = LIST(range(5))
    my_list[2] = 77
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 77
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_set_on_the_edges():
    my_list = LIST(range(5))
    my_list[0] = 77
    my_list[4] = 78
    assert my_list[0] == 77
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 78


def test_set_negative_indexes():
    my_list = LIST(range(5))
    my_list[-1] = 77
    my_list[-2] = 78
    my_list[-3] = 79
    my_list[-4] = 80
    my_list[-5] = 81
    assert my_list[0] == 81
    assert my_list[1] == 80
    assert my_list[2] == 79
    assert my_list[3] == 78
    assert my_list[4] == 77


def test_set_index_out_of_range():
    my_list = LIST(range(5))
    with pytest.raises(IndexError):
        my_list[5] = 77

    with pytest.raises(IndexError):
        my_list[17] = 77

    with pytest.raises(IndexError):
        my_list[-6] = 77

    with pytest.raises(IndexError):
        my_list[-100] = 77


def test_set_wrong_type():
    my_list = LIST(range(5))
    with pytest.raises(TypeError):
        my_list[1.0] = 77

    with pytest.raises(TypeError):
        my_list["asd"] = 77


def test_get_in_the_middle():
    my_list = LIST("rudolf")

    value = my_list[2]
    assert value == "d"


def test_get_on_the_edges():
    my_list = LIST("rudolf")
    assert my_list[0] == "r"
    assert my_list[5] == "f"


def test_get_negative_indexes():
    max_range = 5
    my_list = LIST(range(max_range))
    last: int = my_list[-1]
    assert last == max_range - 1

    my_list[-1] = 33333
    assert my_list[-1] == 33333

    my_list[-4] = -4
    assert my_list[-4] == -4


def test_get_wrong_type():
    my_list = LIST(range(5))
    with pytest.raises(TypeError):
        print(my_list[1.0])

    with pytest.raises(TypeError):
        print(my_list["asd"])


def test_get_index_error():
    my_list = LIST(range(5))
    with pytest.raises(IndexError):
        print(my_list[5])

    with pytest.raises(IndexError):
        print(my_list[17])

    with pytest.raises(IndexError):
        print(my_list[-6])

    with pytest.raises(IndexError):
        print(my_list[-100])


def test_get_slicing_positive():
    max_range = 30_000
    my_list = LIST(range(max_range))

    print(my_list[:10])

    first: int = my_list[0]
    assert first == 0
    my_list[0] = -100
    assert my_list[0] == -100

    last: int = my_list[-1]
    assert last == max_range - 1

    my_list[-1] = 33333
    assert my_list[-1] == 33333

    fifth: int = my_list[5]
    print(fifth)
    assert fifth == 5

    my_list[5] = -4
    assert my_list[5] == -4

    sliced: LIST = my_list[9_000:10_000:100]
    assert len(sliced) == 10
    assert sliced == LIST([9_000, 9_100, 9_200, 9_300, 9_400, 9_500, 9_600, 9_700, 9_800, 9_900])
    summed = sum(sliced)
    assert summed == 94500


def test_get_negative_slicing():
    my_list = LIST(range(5))

    res = my_list[::-1]
    assert res == LIST([4, 3, 2, 1, 0])

    res = my_list[-3:2]
    assert res == LIST([])

    res = my_list[-3:-1]
    assert res == LIST([2, 3])


def test_iter():
    input_str = "rudolf"
    my_list = LIST(input_str)

    for exp, act in zip(input_str, my_list):
        assert exp == act


def test_append():
    my_list = LIST()

    for i in range(5):
        my_list.append(i)

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_extend():
    my_list = LIST()
    my_list.extend(range(5))

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_insert_at_the_front():
    my_list = LIST()

    for i in reversed(range(5)):
        my_list.insert(0, i)

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_insert_at_the_back():
    my_list = LIST()

    for i in range(5):
        my_list.insert(len(my_list), i)

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_insert_at_the_back():
    my_list = LIST()

    for i in range(5):
        my_list.insert(len(my_list), i)

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3
    assert my_list[4] == 4


def test_insert_middle():
    my_list = LIST(range(4))

    my_list.insert(2, 5)

    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 5
    assert my_list[3] == 2
    assert my_list[4] == 3


def test_remove():
    my_list = LIST(chain(range(3), range(3)))
    my_list.remove(2)
    assert len(my_list) == 5
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 0
    assert my_list[3] == 1
    assert my_list[4] == 2


def test_remove_missing_value():
    my_list = LIST(range(5))

    with pytest.raises(ValueError):
        my_list.remove(6)


def test_pop_from_end():
    my_list = LIST(range(5))

    result = my_list.pop()
    assert result == 4
    assert len(my_list) == 4
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 2
    assert my_list[3] == 3


def test_pop_from_end_multiple():
    my_list = LIST(range(5))

    for exp in reversed(range(5)):
        result = my_list.pop()
        assert exp == result


def test_pop_from_middle():
    my_list = LIST(range(5))

    result = my_list.pop(2)
    assert result == 2
    assert len(my_list) == 4
    assert my_list[0] == 0
    assert my_list[1] == 1
    assert my_list[2] == 3
    assert my_list[3] == 4


def test_pop_index_out_of_range():
    with pytest.raises(IndexError):
        my_list = LIST()
        my_list.pop()

    with pytest.raises(IndexError):
        my_list = LIST(range(5))
        my_list.pop(5)


def test_clear():
    my_list = LIST(range(5))
    my_list.clear()
    assert len(my_list) == 0

    for v in my_list:
        assert v == 7


def test_index():
    my_list = LIST(chain(range(3), range(3)))

    result = my_list.index(2)
    assert result == 2


def test_index_with_start_end():
    my_list = LIST(chain(range(3), range(3)))

    result = my_list.index(2, 3)
    assert result == 5

    with pytest.raises(ValueError):
        result = my_list.index(2, 3, -1)
        assert result == 5


def test_count():
    my_list = LIST("hello")

    count = my_list.count("l")
    assert count == 2

    count = my_list.count("z")
    assert count == 0


def test_sort():
    my_list = LIST()
    my_list.sort()
    assert len(my_list) == 0

    my_list = LIST("Hello World!")
    my_list.sort(key=str.lower, reverse=True)
    assert "".join(my_list) == "WroolllHed! "


def test_reverse():
    my_list = LIST()
    my_list.sort()
    assert len(my_list) == 0

    my_list = LIST("Hello World!")
    my_list.reverse()
    assert "".join(my_list) == "!dlroW olleH"


def test_copy():
    my_list = LIST("Hello World!")
    my_list_copy = my_list.copy()
    assert id(my_list_copy) != id(my_list)
    assert my_list_copy[0] == my_list[0]
    assert my_list_copy[0] is my_list[0]
    assert id(my_list_copy[0]) == id(my_list[0])


def test__eq__():
    my_list = LIST("Hello World!")
    my_list_2 = LIST("Hello World!")

    assert my_list == my_list_2
    assert id(my_list) != id(my_list_2)


def test__eq__empty():
    my_list = LIST()
    my_list_2 = LIST()

    assert my_list == my_list_2
    assert id(my_list) != id(my_list_2)


def test__bool__():
    my_list = LIST(range(5))
    assert bool(my_list)

    my_list = LIST()
    assert not bool(my_list)


def test__reversed__():
    my_list = LIST(range(5))
    my_list = reversed(my_list)

    exp = reversed(range(5))
    for exp, act in zip(exp, my_list):
        assert exp == act


def test__contains__():
    my_list = LIST(range(5))

    assert 0 in my_list
    assert 1 in my_list
    assert 2 in my_list
    assert 3 in my_list
    assert 4 in my_list
    assert 5 not in my_list


def test__add__():
    my_list = LIST(range(3))
    my_list2 = LIST(range(3))

    my_list3 = my_list + my_list2
    assert len(my_list3) == 6
    assert my_list3[0] == 0
    assert my_list3[1] == 1
    assert my_list3[2] == 2
    assert my_list3[3] == 0
    assert my_list3[4] == 1
    assert my_list3[5] == 2


def test__mul__single_element():
    my_list = LIST([1]) * 4
    assert len(my_list) == 4
    assert my_list[0] == 1
    assert my_list[1] == 1
    assert my_list[2] == 1
    assert my_list[3] == 1


def test__mul__multi_element():
    my_list = LIST([1, 2, 3]) * 2
    assert len(my_list) == 6
    assert my_list[0] == 1
    assert my_list[1] == 2
    assert my_list[2] == 3
    assert my_list[3] == 1
    assert my_list[4] == 2
    assert my_list[5] == 3
# TODO: check __eq__ and other list dunder methods and then create benchmark


def test__str__ints():
    my_list = LIST(range(5))
    txt = str(my_list)
    assert txt == "[0, 1, 2, 3, 4]" 


def test__str__strings():
    my_list = LIST("hello")
    txt = str(my_list)
    assert txt == "['h', 'e', 'l', 'l', 'o']" 


def test__str__custom_type_without_str_and_repr():
    class Item:
        pass

    my_list = LIST([Item(), Item()])
    txt = str(my_list)
    pattern = r"<GeminiRf.test_list.test__str__custom_type_without_str_and_repr.<locals>.Item object at "

    assert txt.count(pattern) == 2


def test__str__custom_type_with_str():
    class Item:
        def __str__(self) -> str:
            return f"{self.__class__.__name__}()"

    my_list = LIST([Item(), Item()])
    txt = str(my_list)
    pattern = r"<GeminiRf.test_list.test__str__custom_type_with_str.<locals>.Item object at "

    assert txt.count(pattern) == 2


def test__str__custom_type_with_repr():
    class Item:
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}()"

    my_list = LIST([Item(), Item()])
    txt = str(my_list)

    assert txt == "[Item(), Item()]" 
