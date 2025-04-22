#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_two(a: list[int], b: list[int]) -> list[list[int]]:
    """
    合并两个区间
    """
    real_a = a
    real_b = b

    # 确保 a 是最小的
    if a[0] > b[0]:
        real_a = b
        real_b = a

    if real_a[1] >= real_b[0]:
        return [[real_a[0], max(real_a[1], real_b[1])]]

    return [real_a, real_b]


def solution(intervals: list[list[int]]) -> list[list[int]]:
    """
    合并多个有序区间
    """
    n = len(intervals)
    if n <= 1:
        return intervals.copy()

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    res: list[list[int]] = [sorted_intervals.pop(0)]

    while len(sorted_intervals):
        last_one = res.pop()
        cur = sorted_intervals.pop(0)
        res.extend(merge_two(last_one, cur))

    return res


if __name__ == "__main__":
    print(solution([[1, 3], [2, 6], [8, 10], [15, 18]]))
