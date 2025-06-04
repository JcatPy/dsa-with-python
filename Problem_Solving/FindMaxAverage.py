def findMaxAverage(nums, k):
    n = len(nums)
    curr_sum = sum(nums[:k])
    average_sum = curr_sum

    for j in range(k, n):
        curr_sum += nums[j]
        curr_sum -= nums[j - k]

        average_sum = max(average_sum, curr_sum)

    return average_sum / float(k)
