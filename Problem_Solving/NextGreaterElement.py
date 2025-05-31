def nextGreaterElements(self, nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(0, 2 * n):
        if i < n:
            while stack and nums[i] > nums[stack[-1]]:
                prev = stack.pop()
                result[prev] = nums[i]
            stack.append(i)
        else:
            while stack and nums[i % n] > nums[stack[-1]]:
                prev = stack.pop()
                result[prev] = nums[i % n]

    return result






