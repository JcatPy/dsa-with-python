from collections import Counter, defaultdict
def minWindow(s, t):
    if len(t) > len(s):
        return ""

    if len(t) == 1 and t in s:
        return t

    target = Counter(t)
    win = defaultdict(int)
    required = len(target)
    formed = 0
    size = float('inf')
    l = 0
    best_l = best_r = 0

    for r, val in enumerate(s):
        win[val] += 1

        if win[val] == target[val]:
            formed += 1

        while formed == required:
            if r - l + 1 < size:
                size = r - l + 1
                best_l, best_r = l, r

            win[s[l]] -= 1

            if win[s[l]] < target[s[l]]:
                formed -= 1

            l += 1

    return "" if size == float('inf') else s[best_l: best_r + 1]




