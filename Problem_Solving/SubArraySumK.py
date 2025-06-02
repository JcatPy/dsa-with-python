def subarraySum(self, nums, k):
    prefix_sum = 0
    prefix_sums = {0:1}
    count = 0

    for i in nums:
        prefix_sum += i
        if prefix_sum - k in prefix_sums:
            count += prefix_sums[prefix_sum - k]
        prefix_sums[prefix_sum] += 1

    return count