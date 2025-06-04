def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr = 0
    curr_sum = 0
    max_sum = float('-inf')
    n = len(nums)

    while curr < n:
        curr_sum += nums[curr]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

        curr += 1

    return max_sum


