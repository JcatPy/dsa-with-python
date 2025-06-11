from collections import defaultdict
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = defaultdict(int)
    id = 0
    n = len(nums)
    for i in range(n):
        if nums[i] not in seen:
            seen[nums[i]] = 1
            nums[id] = nums[i]
            id += 1

        elif nums[i] in seen:
            if seen[nums[i]] == 2:
                continue
            else:
                seen[nums[i]] += 1
                nums[id] = nums[i]
                id += 1

    return id