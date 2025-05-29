def threeSum(self, nums):
    nums.sort()  # O(n log n)
    n = len(nums)
    res = []

    for i in range(n - 2):  # last two positions need l & r
        # --- skip duplicate pivots ---
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:  # found a triplet
                res.append([nums[i], nums[l], nums[r]])

                # --- skip duplicates on l and r ---
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1

            elif s < 0:  # need a bigger sum
                l += 1
            else:  # need a smaller sum
                r -= 1

    return res
