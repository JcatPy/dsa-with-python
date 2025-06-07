# LeetCode 875. Koko Eating Bananas
import math

def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    if h == len(piles):
        return max(piles)

    low = math.ceil(sum(piles) / float(h))
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2

        if sum(map(lambda x: math.ceil(float(x) / mid), piles)) <= h:
            high = mid - 1
        else:
            low = mid + 1

    return int(low)