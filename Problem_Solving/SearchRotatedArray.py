def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    mid = 0

    while (low <= high):
        mid = low + (high - low) // 2

        if target == nums[mid]:
            return mid

        elif nums[low] <= nums[mid]:
            if target >= nums[low] and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if target >= nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
