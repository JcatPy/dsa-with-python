def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    index = 0
    d1 = {}
    for i in nums:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1

    for key, value in d1.items():
        if value > count:
            count = value
            index = key

    return index