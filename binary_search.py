# Classic binary search
def binary_search(nums: list, target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return -1

# Binary search for a rotated array
def rotated_binary_search(nums: list, target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target < nums[mid] or target > nums[high]:
                high = mid - 1
            else:
                low = mid + 1
    return -1