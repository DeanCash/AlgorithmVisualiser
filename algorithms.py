from typing import List
import random
import itertools

def bubble_sort(array: List[int]):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False


        if already_sorted:
            raise StopIteration

        # yield the new array so the visualiser can update the screen
        yield array


# TODO
def quicksort(array: List[int]):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        raise StopIteration

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
            
    yield list(itertools.chain(low, same, high))
        
    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)




