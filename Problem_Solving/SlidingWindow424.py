def characterReplacement(s, k):
    if not s:
        return 0

    freq = [0] * 26  # counts of letters in current window
    best = 0
    L = 0
    maxFreq = 0
    for i, value in enumerate(s):
        freq[ord(value) - 65] += 1
        maxFreq = max(maxFreq, freq[ord(value) - 65])

        while ((i - L + 1) - maxFreq) > k:
            freq[ord(s[L]) - 65] -= 1
            L += 1

        best = max(best, i - L + 1)

    return best
