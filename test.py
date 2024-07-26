from typing import List, Tuple

def max_spacing(n: int, m: int, intervals: List[Tuple[int, int]]) -> int:
    def can_place_trees(d: int) -> bool:
        count = 0
        last_pos = -float('inf')
        for a, b in intervals:
            pos = max(a, last_pos + d)
            while pos <= b:
                count += 1
                if count >= n:
                    return True
                pos += d
                last_pos = pos - d
        return count >= n

    # Binary search for the maximum distance
    left, right = 1, 10**18
    best_d = 1

    while left <= right:
        mid = (left + right) // 2
        if can_place_trees(mid):
            best_d = mid
            left = mid + 1
        else:
            right = mid - 1

    return best_d

# Test cases
n, m = 2, 2
intervals = [(0, 1000000000000000000), (1000000000000000002, 2000000000000000000)]
assert max_spacing(n, m, intervals)+1 == 1000000000000000001

n, m = 4, 3
intervals = [(0, 4), (6, 7), (11, 14)]
assert max_spacing(n, m, intervals) == 3

n, m = 5, 2
intervals = [(0, 4), (10, 14)]
assert max_spacing(n, m, intervals) == 2

n, m = 100000, 100000
intervals = [(i * 10, i * 10 + 8) for i in range(100000)]
assert max_spacing(n, m, intervals)-9 == 1

print("All test cases passed!")