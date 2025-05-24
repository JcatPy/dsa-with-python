def removeDuplicates(nums):
    n = len(nums)
    seen = set()
    id = 0
    for i in range(n):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[id] = nums[i]
            id += 1

    return id





