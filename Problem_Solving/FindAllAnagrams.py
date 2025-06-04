from collections import Counter
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    count_p = Counter(p)
    result = []
    len_p = len(p)
    len_s = len(s)
    window_count = Counter(s[:len_p])

    if count_p == window_count:
        result.append(0)

    for i in range(len_p, len_s):
        window_count[s[i]] += 1
        window_count[s[i - len_p]] -= 1

        if window_count[s[i - len_p]] == 0:
            del window_count[s[i - len_p]]

        if window_count == count_p:
            result.append(i - len_p + 1)

    return result