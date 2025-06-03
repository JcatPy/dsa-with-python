def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    balance_first = {0: -1}
    balance = max_len = 0
    for i, num in enumerate(nums):
        balance += 1 if num == 1 else -1

        if balance in balance_first:
            max_len = max(max_len, i - balance_first[balance])

        else:
            balance_first[balance] = i

    return max_len
