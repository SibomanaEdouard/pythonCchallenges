# def can_place_balls(balls, positions, min_dist):
#     count = 1  # First ball placed at the first position
#     last_position = positions[0]

#     for i in range(1, len(positions)):
#         if positions[i] - last_position >= min_dist:
#             count += 1
#             last_position = positions[i]
#             if count == balls:
#                 return True
#     return False

# def find_largest_min_dist(balls, positions):
#     positions.sort()
#     low = 1
#     high = positions[-1] - positions[0]
#     result = 0

#     while low <= high:
#         mid = (low + high) // 2
#         print(f"Trying distance: {mid}")

#         if can_place_balls(balls, positions, mid):
#             result = mid
#             low = mid + 1
#         else:
#             high = mid - 1

#     return result

# def main():
#     test_cases = [
#         {"balls": 2, "positions": [1, 1000000000000000000], "expected": 999999999999999999},
#         {"balls": 2, "positions": [2, 2], "expected": 0},
#         {"balls": 2, "positions": [1, 3, 4], "expected": 3}
#     ]

#     for i, test_case in enumerate(test_cases):
#         result = find_largest_min_dist(test_case["balls"], test_case["positions"])
#         print(f"Test case {i + 1}: Expected {test_case['expected']}, Got {result}")

# if __name__ == "__main__":
#     main()
