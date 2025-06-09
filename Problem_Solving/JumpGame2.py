# Greedy problem
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    farthest = 0
    jumps = 0
    current_end = 0
    n = len(nums)

    if n <= 1:  # already at last index
        return 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps

    return jumps