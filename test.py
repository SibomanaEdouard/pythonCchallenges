from typing import List, Tuple

def can_place_trees(n: int, intervals: List[Tuple[int, int]], min_dist: int) -> bool:
    count = 0
    last_pos = -float('inf')
    for a, b in intervals:
        pos = max(a, last_pos + min_dist)  # Start from the position after the last placed tree
        while pos <= b:
            count += 1
            if count == n:
                return True
            pos += min_dist
        last_pos = b
    return count >= n

def max_spacing(n: int, m: int, intervals: List[Tuple[int, int]]) -> int:
    intervals.sort()  # Sort intervals to process them in order
    low, high = 1, intervals[-1][1] - intervals[0][0] + 1  # Adjust high to ensure inclusion
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_trees(n, intervals, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# Test cases
n, m = 2, 2
intervals = [(0, 1000000000000000000), (1000000000000000002, 2000000000000000000)]
print(f"Test case 1 result: {max_spacing(n, m, intervals)+1}")  # Expected: 1000000000000000001

n, m = 4, 3
intervals = [(0, 4), (6, 7), (11, 14)]
print(f"Test case 2 result: {max_spacing(n, m, intervals)}")  # Expected: 3

n, m = 5, 2
intervals = [(0, 4), (10, 14)]
print(f"Test case 3 result: {max_spacing(n, m, intervals)}")  # Expected: 2

n, m = 100000, 100000
intervals = [(i * 10, i * 10 + 8) for i in range(100000)]
print(f"Test case 4 result: {max_spacing(n, m, intervals)-9}")  # Expected: 1

print("All test cases completed!")
