#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def quick_sort(arr: list[int]) -> list[int]:
    """
    快排
    """
    arr_length = len(arr)
    if arr_length <= 1:
        return arr.copy()

    left: list[int] = list()
    right: list[int] = list()
    pivot = arr[0]

    for i in range(1, arr_length):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left).extend([pivot]).extend(quick_sort(right))


if __name__ == "__main__":
    print(quick_sort([2, 1, 5, 3, 8, 4, 9, 5]))
