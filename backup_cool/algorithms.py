from typing import List, Any

def bubble_sort(array: List[Any]):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
                
                # yield new array so the visualiser can update the screen
                yield array

        if already_sorted:
            raise StopIteration







