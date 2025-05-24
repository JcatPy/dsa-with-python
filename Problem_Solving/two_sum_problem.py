def twoSum(nums, target):
    complement = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in complement:
            return [complement[diff], index]
        complement[value] = index