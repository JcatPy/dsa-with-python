def productExceptSelf(self, nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    suffix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    for j in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


