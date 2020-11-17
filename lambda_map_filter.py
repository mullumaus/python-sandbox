#!/usr/bin/env python3
# Test lambda
add = lambda x, y: x + y


# map functions expect a function object and any number of iterables,
# such as list, dictionary, etc. It executes the function_object for
# each element in the sequence and returns a list of the elements
# modified by the function object.
def multiply2(x):
    return x * 2


def multi_map():
    list_a = [1, 2, 3]
    list_b = [10, 20, 30]
    result = list(map(lambda x, y: x + y, list_a, list_b))
    print(result)


# The filter function expects two arguments: function_object and an iterable.
# function_object returns a boolean value and is called for each element of
# the iterable. filter returns only those elements for which the function_
# object returns True.
def filter_func():
    a = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 2 == 0, a))
    print(result)


if __name__ == "__main__":
    print(add(2, 3))
    list_map = list(map(multiply2, [1, 2, 3, 4]))
    print(list_map)
    print(list(map(lambda x: x * 2, [1, 2, 3, 4])))
    multi_map()
    filter_func()
