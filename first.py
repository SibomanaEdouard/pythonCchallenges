from typing import List, Tuple

def max_spacing(n: int, m: int, intervals: List[Tuple[int, int]]) -> int:
    intervals.sort()

    def count_trees(distance: int) -> int:
        count = 0
        last_pos = float('-inf')
        for start, end in intervals:
            pos = max(start, last_pos + distance)
            while pos <= end:
                count += 1
                last_pos = pos
                pos += distance
        return count

    left, right = 0, intervals[-1][1] - intervals[0][0]
    while left < right:
        mid = left + (right - left + 1) // 2
        if count_trees(mid) >= n:
            left = mid
        else:
            right = mid - 1

    return left

# Test cases
def run_tests():
    # Test case 1
    n, m = 2, 2
    intervals = [(0, 1000000000000000000), (1000000000000000002, 2000000000000000000)]
    assert max_spacing(n, m, intervals) == 1000000000000000001

    # Test case 2
    n, m = 4, 3
    intervals = [(0, 4), (6, 7), (11, 14)]
    assert max_spacing(n, m, intervals) == 3

    # Test case 3
    n, m = 5, 2
    intervals = [(0, 4), (10, 14)]
    assert max_spacing(n, m, intervals) == 2

    # Test case 4
    n, m = 100000, 100000
    intervals = [(i * 10, i * 10 + 8) for i in range(100000)]
    assert max_spacing(n, m, intervals) == 1

    print("All test cases passed!")

run_tests()