
from typing import List

def dynamic_sliding_window(arr: List[int], target: int) -> int:
   
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink window if the while condition satisfies
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return 0 if min_length == float("inf") else min_length


# Example
if __name__ == "__main__":
    arr = [2, 3, 1, 2, 4, 3]
    target = 7

    print("Array:", arr)
    print("Target:", target)
    print("Smallest subarray length:", dynamic_sliding_window(arr, target))